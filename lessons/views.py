# from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.contrib import messages
# from django.db.models import Q
# from . models import Instrument, Lesson, Image,Subscription


# # Finds image, if exists or returns a blank
# # returns a None if blank is also missing
# def findImage(image):
#     image = Image.objects.filter(name=image)
#     if not image:
#         image = Image.objects.filter(name="blank")
#     if not image:
#         image = None
#         return image
#     else:
#         image = image.get()
#         return image


# # Creates a list to be returned for entery into a dictionary
# def createDictList(dictionary):
#     dictList = []
#     for x in dictionary:
#         dictList.append(x)
#     return dictList


# def lessons(request):
#     """ This view returns the all instrument specific lessons """

#     lessons = Lesson.objects.all()
#     instruments = None
#     query = None

#     # Used by user search bar
#     if request.GET:
#         if 'instrument' in request.GET:
#             instruments = request.GET['instrument']
#             lessons = lessons.filter(instrument__name=(instruments))

#         if 'userquery' in request.GET:
#             query = request.GET['userquery']
#             if not query:
#                 messages.info(request, "No search information input!")
#                 return redirect(reverse('lessons'))

#             queries = Q(instrument__name__icontains=query) | Q(name__icontains=query)
#             lessons = lessons.filter(queries)

#     for lesson in lessons:
#         lesson.image = findImage(lesson.image)

#     context = {
#         'lessons': lessons,
#     }

#     return render(request, 'lessons/lessons.html', context)


# def subscriptions(request):
#     """ This view returns the all current specials/subscriptions offered """

#     subscriptions = Subscription.objects.all()

#     # Creates iterable lists in subscription objects
#     for subscription in subscriptions:
#         # Queries foreign and manytomany fields
#         subscription.image = findImage(subscription.image)
#         subscription.instruments = createDictList(subscription.instrument.all())
#         subscription.instrument_levels = createDictList(subscription.instrument_level.all())

#     context = {
#         'subs': subscriptions,
#     }

#     return render(request, 'lessons/subscriptions.html', context)


# def details(request, sub_id):
#     """
#     This view returns a selection screen for users to select options
#     offered for specific lessons/sepcials/subscriptions
#     """

#     if request.GET:
#         if 'subscription' in request.GET:
#             lesson = get_object_or_404(Subscription, pk=sub_id)
#             lesson.instruments = createDictList(lesson.instrument.all())
#             lesson.instrument_levels = createDictList(lesson.instrument_level.all())
#             lesson.lesson = False

#         elif 'lesson' in request.GET:
#             lesson = get_object_or_404(Lesson, pk=sub_id)
#             lesson.instruments = lesson.instrument
#             lesson.instrument_levels = lesson.instrument_level
#             lesson.lesson = True

#         else:
#             messages.error(request, "Sorry, something went wrong!")
#             return redirect('lessons')

#     lesson.image = findImage(lesson.image)
#     lesson.lesson_style = createDictList(lesson.class_type.all())
#     lesson.sub_duration = createDictList(lesson.subscription_months.all())
#     lesson.per_week = createDictList(lesson.lessons_per_week.all())
#     lesson.minutes = createDictList(lesson.lesson_minutes.all())

#     context = {
#         'lesson': lesson
#     }

#     return render(request, 'lessons/details.html', context)