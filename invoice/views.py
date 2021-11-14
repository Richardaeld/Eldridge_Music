from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, redirect, reverse
from django.views.decorators.http import require_POST
from django.contrib import messages

from django.conf import settings
from shopping_bag.contexts import cart_contents
from .forms import InvoiceForm
from profile_history.forms import User_Profile_History_Form
from profile_history.models import User_Profile_History
from merchandise.models import Merch
from .models import Invoice, InvoiceLineItem

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        print(pid)
        print(stripe.api_key)
        print(intent)

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, (
            'Your invoice cannot be processed '
            'right now. Try again later.'
        ))
        return HttpResponse(content=e, status=400)


def invoice(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'city': request.POST['city'],
            'street_address_billing': request.POST['street_address_billing'],
            'street_address_shipping': request.POST['street_address_shipping'],
            'state_county': request.POST['state_county'],
            'post_code': request.POST['post_code'],
            'country': request.POST['country'],
        }
        invoice_form = InvoiceForm(form_data)
        if invoice_form.is_valid():
            invoice = invoice_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            invoice.strip_pid = pid
            invoice.original_cart = json.dumps(cart)
            invoice.save()
            for item_id, item_data in cart.items():
                try:
                    item = Merch.objects.get(id=item_id)
                    invoice_line_item = InvoiceLineItem(
                        invoice=invoice,
                        item=item,
                        amount=item_data,
                    )
                    invoice_line_item.save()
                except Merch.DoesNotExist:
                    messages.error(request, (
                        "One of the products in you bag wasn't found "
                        "in our database. Please call us for help!"
                    ))
                    invoice.delete()
                    return redirect(reverse('shopping_bag'))

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse(
                'checkout_success', args=[invoice.invoice_number]))

        else:
            messages.error(request, (
                'There was an error with your form submission '
                'please check your form information'
            ))

    else:

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is currently empty")
            return redirect(reverse('merchandise'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = User_Profile_History.objects.get(user=request.user)
                invoice_form = InvoiceForm(initial={
                    'name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone': profile.default_phone,
                    'city': profile.default_city,
                    'street_address_billing': profile.default_street_address_billing,
                    'street_address_shipping': profile.default_street_address_shipping,
                    'state_county': profile.default_state_county,
                    'post_code': profile.default_post_code,
                    'country': profile.default_country,
                })
            except User_Profile_History.DoesNotExist:
                invoice_form = InvoiceForm()
        else:
            invoice_form = InvoiceForm()

    if not stripe_secret_key:
        messages.warning(request, 'Stripe Public key is missing.')

    MEDIA_URL = settings.MEDIA_URL
    template = "invoice/invoice.html"
    context = {
        'MEDIA_URL': MEDIA_URL,
        'invoice_form': invoice_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, invoice_number):
    """
    Shows a success page for processed orders
    """

    save_info = request.session.get('save_info')
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)

    if request.user.is_authenticated:
        profile = User_Profile_History.objects.get(user=request.user)
        # This attaches user's profile to order
        invoice.user_profile = profile
        invoice.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone': invoice.phone,
                'default_city': invoice.city,
                'default_street_address_billing': invoice.street_address_billing,
                'default_street_address_shipping': invoice.street_address_shipping,
                'default_state_county': invoice.state_county,
                'default_post_code': invoice.post_code,
                'default_country': invoice.country,
            }
            user_profile_history_form = User_Profile_History_Form(
                profile_data, instance=profile)
            if user_profile_history_form.is_valid():
                user_profile_history_form.save()

    messages.success(request, (
        f'Your Invoice was successfully processed! '
        f'Your invoice number is {invoice_number}. A Confirmation '
        f'email will be sent to {invoice.email}'
    ))

    if 'cart' in request.session:
        del request.session['cart']

    template = 'invoice/checkout_success.html'
    context = {
        'invoice': invoice,
    }

    return render(request, template, context)
