from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from merchandise.forms import MerchForm
from .models import Merch
from django.conf import settings


def merchandise(request):

    merch = Merch.objects.all()

    # Used by user search bar
    if request.GET:
        if 'genre' in request.GET:
            genre = request.GET['genre']
            merch = merch.filter(style__style=(genre))

        if 'userquery' in request.GET:
            query = request.GET['userquery']
            if not query:
                messages.info(request, "No search information input!")
                return redirect(reverse('merchandise'))

            queries = Q(name__icontains=query) | Q(author__icontains=query)
            merch = merch.filter(queries)

    MEDIA_URL = settings.MEDIA_URL
    template = 'merchandise/merchandise.html'

    context = {
        'MEDIA_URL': MEDIA_URL,
        'merchandise': merch,
    }

    return render(request, template, context)


def specials(request):

    merch = Merch.objects.all()

    merch = merch.filter(special=True)

    MEDIA_URL = settings.MEDIA_URL
    template = 'merchandise/merchandise.html'

    context={
        'MEDIA_URL': MEDIA_URL,
        'merchandise': merch,
    }

    return render(request, template, context)


def details(request, merch_id):

    merch = get_object_or_404(Merch, pk=merch_id)

    MEDIA_URL = settings.MEDIA_URL
    template = 'merchandise/details.html'

    context = {
        'MEDIA_URL': MEDIA_URL,
        'merch': merch,
    }

    return render(request, template, context)


def add_merch(request):
    """
    Allow superuser to add merchandise to store
    """

    if request.method == 'POST':
        form = MerchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created merchandise')
            return redirect(reverse('add_merch'))
        else:
            messages.error(request, 'Failed to add merchandise. Please check the form for validity')
    else:
        form = MerchForm()

    template = 'merchandise/add_merch.html'
    context = {
        "no_cart": True,
        'form': form,
    }

    return render(request, template, context)