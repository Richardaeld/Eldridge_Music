from django.shortcuts import get_object_or_404, render
from .models import Merch

def merchandise(request):

    merch = Merch.objects.all()

    template = 'merchandise/merchandise.html'

    context = {
        'merchandise': merch,
    }

    return render(request, template, context)


def details(request, merch_id):

    merch = get_object_or_404(Merch, pk=merch_id)

    template = 'merchandise/details.html'

    context = {
        'merch': merch,
    }

    return render(request, template, context)