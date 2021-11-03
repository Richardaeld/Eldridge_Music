from django.shortcuts import render, get_object_or_404,redirect, reverse
# from lessons.models import Lesson, Subscription, Image
from profile_history.models import User_Profile_History
from .forms import InvoiceForm
# from lessons.views import findImage, createDictList
# from lessons.models import Lesson, Subscription
from django.contrib import messages


def invoice(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty")
        return redirect(reverse('merchandise'))

    invoice_form = InvoiceForm()
    template = "invoice/invoice.html"
    context = {
        'invoice_form': invoice_form,
    }

    return render(request,template, context)



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