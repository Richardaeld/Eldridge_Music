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
        instruments = []
        for each_instrument in subscription.instrument.all():
                instruments.append(each_instrument)
        subscription.instruments = instruments

        # Create list for instrument levels
        instrument_levels = []
        for levels in subscription.instrument_level.all():
            instrument_levels.append(levels)
        subscription.instrument_levels = instrument_levels

        # create list for lesson types
        # lesson_type = []
        # for lesson_types in subscription.lesson_class_type.all():
        #     lesson_type.append(lesson_types)
        # subscription.lesson_type = lesson_type

    context = {
        'subs': subscriptions,
    }

    return render(request, 'lessons/subscriptions.html', context)


def details(request, sub_id):

    if request.GET:
        if 'subscription' in request.GET:
            lesson = get_object_or_404(Subscription, pk=sub_id)

            # Create list for offered instruments
            instruments = []
            for each_instrument in lesson.instrument.all():
                    instruments.append(each_instrument)
            lesson.instruments = instruments
            lesson.lesson = False

            # Create list for instrument levels
            instrument_levels = []
            for levels in lesson.instrument_level.all():
                instrument_levels.append(levels)
            lesson.instrument_levels = instrument_levels

        elif 'lesson' in request.GET:
            lesson = get_object_or_404(Lesson, pk=sub_id)
            lesson.instruments = lesson.instrument
            lesson.instrument_levels = lesson.instrument_level
            lesson.lesson = True

        else:
            messages.error(request, "Sorry, something went wrong!")
            return redirect('lessons')

    image = Image.objects.filter(name=lesson.image)
    image = image.get()
    lesson.image = image

    lesson_style = []
    for lesson_type in lesson.class_type.all():
        lesson_style.append(lesson_type)
    lesson.lesson_style = lesson_style

    sub_duration = []
    for duration in lesson.subscription_months.all():
        sub_duration.append(duration)
    lesson.sub_duration = sub_duration

    lesson_per_week = []
    for per_week in lesson.lessons_per_week.all():
        lesson_per_week.append(per_week)
    lesson.per_week = lesson_per_week

    lesson_minutes = []
    for minutes in lesson.lesson_minutes.all():
        lesson_minutes.append(minutes)
    lesson.minutes = lesson_minutes

    context = {
        'lesson': lesson
    }

    print(type(lesson.instruments))

    return render(request, 'lessons/details.html', context)