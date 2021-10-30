from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Merch

def merchandise(request):

    merch = Merch.objects.all()

    # Used by user search bar
    if request.GET:
        # if 'instrument' in request.GET:
        #     instruments = request.GET['instrument']
        #     merch = merch.filter(merchandise__name=(Merchandise))

        if 'userquery' in request.GET:
            query = request.GET['userquery']
            if not query:
                messages.info(request, "No search information input!")
                return redirect(reverse('merchandise'))

            queries = Q(name__icontains=query) | Q(author__icontains=query)
            merch = merch.filter(queries)


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