from django.shortcuts import render
from . models import Instrument, Lesson


def lessons(request):
    """ This view returns the all category specific lessons """

    adminLessons = Lesson.objects.all()



    test = adminLessons
    for le in test:
        # print(le)
        # print(isinstance(le, (float, int, str, list, dict, tuple)))
        # print(type(le))
        # print(le.keys())

        print(le.instrument)
        print(le.instrument_level)
        # if le.instrument_level:
        #     le.instrument_level = str(le.instrument_level)
        # if str(le.instrument_level) == "Beginner":
        #     print("It workded")



    context = {
        'lessons': adminLessons,
    }


    return render(request, 'lessons/lessons.html', context)