from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Instrument, Lesson


def lessons(request):
    """ This view returns the all category specific lessons """

    lessons = Lesson.objects.all()
    instruments = None
    query = None


    for lesson in lessons:
        print(lesson.instrument_level)

    print(lessons.filter(instrument_level__level=("Beginner")))

    if request.GET:
        if 'instrument' in request.GET:
            instruments = request.GET['instrument']
            lessons = lessons.filter(instrument__name=(instruments))



    context = {
        'lessons': lessons,
    }


    return render(request, 'lessons/lessons.html', context)