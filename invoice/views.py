from django.shortcuts import render, get_object_or_404
from lessons.models import Lesson, Subscription, Image
from profile_history.models import User_Profile_History
from .forms import InvoiceForm
from lessons.views import findImage, createDictList

def checkout_lesson(request, lesson_id, lesson_subscription):
    if lesson_subscription:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
    else:
        lesson = get_object_or_404(Subscription, pk=lesson_id)

    ## ----Do Not remove until Image's path to frontend is understood
    # image = Image.objects.filter(name=lesson.image)
    # if not image:
    #     image = Image.objects.filter(name="blank")
    # image = image.get()
    # lesson.image = image
    # lesson.image = findImage(lesson.image)

    if request.method == 'POST':
        lesson_summery = {
            'is_lesson': lesson_subscription,
            # 'is_lesson': request.POST['is_lesson'],
            'prime_key': lesson_id,
            # 'pk': request.POST['pk'],
            'instrument': request.POST['instrument'],
            'level': request.POST['level'],
            'style': request.POST['style'],
            'month_duration': request.POST['month_duration'],
            'per_week': request.POST['per_week'],
            'minutes': request.POST['minutes'],
        }

    # invoice = InvoiceForm()
    template = 'invoice/checkout.html'

    if request.user.is_authenticated:
        user = get_object_or_404(User_Profile_History, user=request.user)
        invoice = InvoiceForm(initial={
            'name': user.default_full_name,
            'email': user.default_email,
            'phone': user.default_phone,
            'city': user.default_city,
            'street_address_billing': user.default_street_address,
            'state_county': user.default_state_county,
            'post_code': user.default_post_code,
            'country': user.default_country,
        })
    else:
        invoice = InvoiceForm()
        user = None

    context = {
        'is_lesson': lesson_subscription, # is lesson or subscription
        'lesson_summery': lesson_summery, # pulls required form information
        'lesson': lesson, # Order informaiton for lesson/subscription
        'user': user, # user informaion
        'invoice': invoice # function for building form
    }

    return render(request, template, context)
