from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Instrument, Lesson, Image


def lessons(request):
    """ This view returns the all category specific lessons """

    lessons = Lesson.objects.all()

    for lesson in lessons:
        image = Image.objects.filter(name=lesson.image)
        image = image.get()
        # print(image.image)
        # lesson.test = image.image
        lesson.test = image

        print(lesson.test)

        # print(base)
        # print(lesson.test)
        # print(Image.objects.filter(name=lesson.image))
    # for lesson in lessons :
    #     for image in lesson.image:
    #         # image.objects.get()
    #         print(image)
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

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            lessons = lessons.filter(queries)


    context = {
        'lessons': lessons,
    }


    return render(request, 'lessons/lessons.html', context)