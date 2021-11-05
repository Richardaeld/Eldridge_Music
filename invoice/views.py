from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, redirect, reverse
from django.conf import settings
from django.views.decorators.http import require_POST
# from lessons.models import Lesson, Subscription, Image
from profile_history.models import User_Profile_History
from .forms import InvoiceForm
# from lessons.views import findImage, createDictList
# from lessons.models import Lesson, Subscription
from django.contrib import messages
from shopping_bag.contexts import cart_contents
from .forms import InvoiceForm
from merchandise.models import Merch
from .models import Invoice, InvoiceLineItem

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Your invoice cannot be processed \
            right now. Try again later.")
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
            invoice = invoice_form.save()
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
                        "One of the products in you bag wasn't found in our database."
                        "Please call us for help!"
                    ))
                    invoice.delete()
                    return redirect(reverse('shopping_bag'))

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse('checkout_success', args=[invoice.invoice_number]))

        else:
            messages.error(request, 'There was an error with your form submission \
                please check your form information')

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


        invoice_form = InvoiceForm()

    if not stripe_secret_key:
        messages.warning(request, 'Stripe Public key is missing.')

    template = "invoice/invoice.html"
    context = {
        'invoice_form': invoice_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request,template, context)


def checkout_success(request, invoice_number):
    """
    Shows a success page for processed orders
    """

    save_info = request.session.get('save_info')
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)
    messages.success(request, f'Your Invoice was successfully processed! \
        Your invoice number is {invoice_number}. A Confirmation \
            email will be sent to {invoice.email}')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'invoice/checkout_success.html'
    context = {
        'invoice': invoice,
    }

    return render(request, template, context)


# def checkout_lesson(request, lesson_id, lesson_sku):
#     # if lesson_sku.find("les") != -1:
#     #     lesson = get_object_or_404(Lesson, pk=lesson_id)
#     # elif lesson_sku.find("sub") != -1:
#     #     lesson = get_object_or_404(Subscription, pk=lesson_id)
#     # else:
#     #     messages.error(request, "An error occurred please try again later")

#     # lesson.image = findImage(lesson.image)

#     # if request.method == 'POST':
    
    
    
#     lesson_summary = {
#         # 'is_lesson': lesson_subscription,
#         # 'is_lesson': request.POST['is_lesson'],
#         # 'prime_key': lesson_id,
#         # 'pk': request.POST['pk'],
#         # 'instrument': request.POST['instrument'],
#         # 'level': request.POST['level'],
#         # 'style': request.POST['style'],
#         # 'month_duration': request.POST['month_duration'],
#         # 'per_week': request.POST['per_week'],
#         # 'minutes': request.POST['minutes'],
#         # 'payment_type': request.POST['payment_type'],
#         # 'price': request.POST['price'],
#         # 'sku': lesson.sku,
#     }

#     # invoice = InvoiceForm()
#     template = 'invoice/checkout.html'

#     if request.user.is_authenticated:
#         user = get_object_or_404(User_Profile_History, user=request.user)
#         invoice = InvoiceForm(initial={
#             'name': user.default_full_name,
#             'email': user.default_email,
#             'phone': user.default_phone,
#             'city': user.default_city,
#             'street_address_billing': user.default_street_address,
#             'state_county': user.default_state_county,
#             'post_code': user.default_post_code,
#             'country': user.default_country,
#         })
#     else:
#         invoice = InvoiceForm()
#         user = None

#     context = {
#         # 'is_lesson': lesson_subscription, # is lesson or subscription
#         'prime_key': lesson_id,
#         'lesson_summary': lesson_summary, # pulls required form information
#         # 'lesson': lesson, # Order informaiton for lesson/subscription
#         'user': user, # user informaion
#         'invoice': invoice # function for building form
#     }

#     return render(request, template, context)


# def record_invoice(request, sku, item_pk):
#     if sku.find("les") != -1:
#         lesson = get_object_or_404(Lesson, pk=item_pk)

#     elif sku.find("sub") != -1:
#         lesson = get_object_or_404(Subscription, pk=item_pk)

#     else:
#         messages.error(request, "An error occurred please try again later")

#     print("--------------------------------")
#     print(lesson)
#     print(request.POST.get('instrument', None))
#     # for check in lesson.instrument:
#     # list_time = list(map(lambda x: str(x), new_time[0:3]))
#     # list_time = list(map(lambda x: str(x), lesson.instrument))
#     # lesson.instruments = createDictList(lesson.instrument.all())
#     # test = createDictList(lesson.instrument.all())
#     # test123 = {
#     #     "something": request.POST['instrument']
#     # }
#     # print(type(request.POST['price']))
#     # print(test123)
#     # print(request.POST.get('month_duration', None))
#     # print(request.POST.get('instrument', None))
#     try:
#         instruments = lesson.instrument
#         # intlist = list(map(lambda x: str(x), test))
#         # print(intlist)
#         print(request.POST['name'], "request")
#         # if intlist.index(request.POST['instrument']):
#             # print("I succeeded")
#     except Exception as error:
#         print("I VALUES ERRORED----------------")
#         print(error)
#         print("I VALUES ERRORED----------------")
#         messages.error(request, "An error occurred please try again later")

#     context= {

#     }

#     return redirect(reverse('home'))