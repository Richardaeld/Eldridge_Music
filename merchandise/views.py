from django.shortcuts import render
from .models import Merch

def merchandise(request):

    merch = Merch.objects.all()

    template = 'merchandise/merchandise.html'

    context = {
        'merchandise': merch,
    }

    return render(request, template, context)