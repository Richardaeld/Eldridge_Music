from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings
from profile_history.models import User_Profile_History
from merchandise.models import Merch
from .models import Invoice, InvoiceLineItem

import json
import time


class StripeWH_Handler:
    """
    Controls webhooks from Stripe
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, invoice):
        """
        Sends a confirmation email to user
        """
        cust_email = invoice.email
        subject = render_to_string(
            'checkout/confirmation_email/confirmation_email_subject.txt',
            {'invoice': invoice}
        )

        body = render_to_string(
            'checkout/confirmation_email/confirmation_email_body.txt',
            {'invoice': invoice, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Contorls generic/unknown/unexpected webhook
        """
        return HttpResponse(
            content=(
                f'Generic/Unknown/Unexpected '
                f'webhook received: {event["type"]}'),
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Contorls payment_intent.succeeded webhook
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # clean data in shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Updates profile information upon save_info being checked
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = User_Profile_History.objects.get(user__username=username)
            if save_info:
                profile.phone__iexact = shipping_details.phone
                profile.country__iexact = shipping_details.address.country
                profile.post_code__iexact = shipping_details.address.postal_code
                profile.city__iexact = shipping_details.address.city
                profile.street_address_billing__iexact = shipping_details.address.line1
                profile.street_address_shipping__iexact = shipping_details.address.line2
                profile.state_county__iexact = shipping_details.address.state
                profile.save()

        invoice_exists = False
        attempt = 1
        while attempt <= 5:

            try:
                invoice = Invoice.objects.get(
                    name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    street_address_billing__iexact=shipping_details.address.line1,
                    street_address_shipping__iexact=shipping_details.address.line2,
                    state_county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    # Is causing dupilicate invoices to be created
                    stripe_pid=pid,
                )

                invoice_exists = True
                break

            except Invoice.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if invoice_exists:
            self._send_confirmation_email(invoice)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    f'SUCCESS: Verified order already in database'),
                status=200)
        else:
            invoice = None
            try:
                invoice = Invoice.objects.create(
                    name=shipping_details.name,
                    email=billing_details.email,
                    user_profile=profile,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    post_code=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    street_address_billing=shipping_details.address.line1,
                    street_address_shipping=shipping_details.address.line2,
                    state_county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    item = Merch.objects.get(id=item_id)
                    invoice_line_item = InvoiceLineItem(
                        invoice=invoice,
                        item=item,
                        amount=item_data,
                    )
                    invoice_line_item.save()
            except Exception as e:
                if invoice:
                    invoice.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(invoice)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | '
                f'SUCCESS: Created invoice in webhooks'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Contorls payement_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
