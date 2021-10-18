from django.shortcuts import render, get_object_or_404
from invoice.forms import InvoiceForm
from lessons.models import Lesson, Subscription, Image
from profile_history.models import User_Profile_History
from .forms import InvoiceForm

def checkout_lesson(request, lesson_id, lesson_subscription):

    user = None
    if request.user != 'AnonymousUser':
        user = get_object_or_404(User_Profile_History, user=request.user)

    if lesson_subscription:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
    else:
        lesson = get_object_or_404(Subscription, pk=lesson_id)

    lesson_subscription = lesson_subscription

    image = Image.objects.filter(name=lesson.image)
    if not image:
        image = Image.objects.filter(name="blank")
    image = image.get()
    lesson.image = image

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

    if lesson_summery:
        print(lesson_summery)

    invoice = InvoiceForm()
    template = 'invoice/checkout.html'

    context = {
        'is_lesson': lesson_subscription,
        'pk': lesson.pk,
        'lesson_summery': lesson_summery,
        'lesson': lesson,
        'lesson_subscription': lesson_subscription,
        'user': user,
        'invoice': invoice
    }

    return render(request, template, context)
