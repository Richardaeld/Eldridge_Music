from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Instrument, Lesson, Image,Subscription


def lessons(request):
    """ This view returns the all category specific lessons """

    lessons = Lesson.objects.all()

    instruments = None
    query = None

    if request.GET:
        if 'instrument' in request.GET:
            instruments = request.GET['instrument']
            lessons = lessons.filter(instrument__name=(instruments))

        if 'userquery' in request.GET:
            query = request.GET['userquery']
            if not query:
                messages.info(request, "No search information input!")
                return redirect(reverse('lessons'))

            queries = Q(instrument__name__icontains=query) | Q(name__icontains=query)
            lessons = lessons.filter(queries)

    for lesson in lessons:
        image = Image.objects.filter(name=lesson.image)
        image = image.get()
        lesson.image = image

    context = {
        'lessons': lessons,
    }

    return render(request, 'lessons/lessons.html', context)


def subscriptions(request):

    subscriptions = Subscription.objects.all()

    # Creates iterable lists in subscription objects
    for subscription in subscriptions:
        # Queries foreign and manytomany fields
        image = Image.objects.filter(name=subscription.image)
        image = image.get()
        subscription.image = image

        # Create list for offered instruments
        instrument = []
        for instruments in subscription.instrument_included.all():
                instrument.append(instruments)
        subscription.instrument = instrument

        # Create list for instrument levels
        instrument_level = []
        for instrument_levels in subscription.level_included.all():
            instrument_level.append(instrument_levels)
        subscription.instrument_level = instrument_level

        # create list for lesson types
        # lesson_type = []
        # for lesson_types in subscription.lesson_class_type.all():
        #     lesson_type.append(lesson_types)
        # subscription.lesson_type = lesson_type

    context = {
        'subs': subscriptions,
    }

    return render(request, 'lessons/subscriptions.html', context)


def subs_details(request, sub_id):

    subscription = get_object_or_404(Subscription, pk=sub_id)

    print(subscription)

    # Creates iterable lists in subscription objects
    # Queries foreign and manytomany fields
    image = Image.objects.filter(name=subscription.image)
    image = image.get()
    subscription.image = image

    # Create list for offered instruments
    instrument = []
    for instruments in subscription.instrument_included.all():
            instrument.append(instruments)
    subscription.instrument = instrument

    # Create list for instrument levels
    instrument_level = []
    for instrument_levels in subscription.level_included.all():
        instrument_level.append(instrument_levels)
    subscription.instrument_level = instrument_level

    context = {
        'sub': subscription
    }

    return render(request, 'lessons/subs_details.html', context)