from django.shortcuts import render
from . models import Instrument, Lesson

def lessons(request):
    """ This view returns the all category specific lessons """
    
    context = {Lesson}
    
    return render(request, 'lessons/lessons.html', context)