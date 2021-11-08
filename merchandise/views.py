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
        if form.is_valid() and request.user.is_superuser:
            item = form.save()
            messages.success(request, 'Successfully created merchandise')
            return redirect(reverse('merch_details', args=[item.id]))
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


def edit_merch(request, merch_id):
    """
    Allow superuser to edit merchandise in store
    """

    item = get_object_or_404(Merch, pk=merch_id)
    form = MerchForm(instnace=item)
    messages.info(request, f'You are editing this: {item.name}')

    if request.method == 'POST':
        form = MerchForm(request.POST, request.FILES, instance=item)
        if form.is_valid() and request.user.is_superuser:
            form.save()
            messages.success(request, 'Successfully updated merchandise')
            return redirect(reverse('details', args=[item.id]))
        else:
            messages.error(request, f'Failed to edit {item.name}. Please check the form for validity')
    else:
        form = MerchForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'merchandise/edit_merch.html'
    context = {
        "no_cart": True,
        'form': form,
        'item': item,
    }

    return render(request, template, context)


def delete_merch(request, merch_id):
    """
    Allow superuser to delete merchandise in store
    """

    if request.user.is_superuser:
        item = get_object_or_404(Merch, pk=merch_id)
        item.delete()
        messages.success(request, 'Merchandise has been deleted!')

    return redirect(reverse('merchandise'))