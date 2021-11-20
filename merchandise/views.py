from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.conf import settings
from merchandise.forms import MerchForm, RatingForm
from profile_history.models import User_Profile_History
from .models import Merch, Merch_Rating
from .rating import add_rating


def merchandise(request):
    """
    Returns a view of all merchandise items
    """
    merch = Merch.objects.all()
    add_rating(merch)

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
    """
    Returns a view of all discounted merchandise items
    """
    merch = Merch.objects.all()
    merch = merch.filter(special=True)
    add_rating(merch)

    MEDIA_URL = settings.MEDIA_URL
    template = 'merchandise/merchandise.html'

    context = {
        'MEDIA_URL': MEDIA_URL,
        'merchandise': merch,
    }

    return render(request, template, context)


def used(request):
    """
    Returns a view of all used merchandise items
    """
    merch = Merch.objects.all()
    merch = merch.filter(used=True)
    add_rating(merch)

    MEDIA_URL = settings.MEDIA_URL
    template = 'merchandise/merchandise.html'

    context = {
        'MEDIA_URL': MEDIA_URL,
        'merchandise': merch,
    }

    return render(request, template, context)


def details(request, merch_id):
    """
    Returns a detailed view of a single merchandise item
    """
    merch = get_object_or_404(Merch, pk=merch_id)
    MEDIA_URL = settings.MEDIA_URL
    template = 'merchandise/details.html'

    avg_rating = 0
    merch_rating_list = []
    all_ratings = Merch_Rating.objects.all().filter(merchandise_id=merch.id)
    for rating in all_ratings:
        merch_rating_list.append(rating.rating)

    number_of_ratings = len(merch_rating_list)
    if number_of_ratings != 0:
        total_rating = sum(merch_rating_list)
        avg_rating = total_rating / number_of_ratings
    merch.avg_rating = avg_rating
    merch.number_of_ratings = number_of_ratings

    context = {
        # "avg_rating": avg_rating,
        'MEDIA_URL': MEDIA_URL,
        'merch': merch,
    }

    return render(request, template, context)


@login_required
def rating_form(request, merch_id):
    """
    Allows users to rate items
    """
    profile = User_Profile_History.objects.get(user=request.user)
    merch = get_object_or_404(Merch, pk=merch_id)
    if request.method == 'POST':
        form_data = {
            'rated_by': profile,
            'rating': request.POST['rating'],
            'merchandise_id': merch,
        }

        try:
            rating = get_object_or_404(Merch_Rating, merchandise_id=merch.id)
            form = RatingForm(form_data, instance=rating)
            if form.is_valid():
                form.save(commit=True)
        except:
            form = RatingForm(form_data)
            if form.is_valid():
                form.save()

    return redirect(reverse('merchandise'))


@login_required
def add_merch(request):
    """
    Allow superuser to add merchandise to store
    """

    if not request.user.is_superuser:
        messages.error(request, "Only store owners are permitted to do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MerchForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_superuser:
            item = form.save()
            messages.success(request, 'Successfully created merchandise.')
            return redirect(reverse('merch_details', args=[item.id]))
        else:
            messages.error(request, (
                'Failed to add merchandise. '
                'Please check the form for validity.'
            ))
    else:
        form = MerchForm()

    template = 'merchandise/add_merch.html'
    context = {
        "no_cart": True,
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_merch(request, merch_id):
    """
    Allow superuser to edit merchandise in store
    """

    if not request.user.is_superuser:
        messages.error(request, "Only store owners are permitted to do that")
        return redirect(reverse('home'))

    item = get_object_or_404(Merch, pk=merch_id)

    if request.method == 'POST':
        form = MerchForm(request.POST, request.FILES, instance=item)
        if form.is_valid() and request.user.is_superuser:
            form.save()
            messages.success(request, 'Successfully updated merchandise')
            return redirect(reverse('merch_details', args=[item.id]))
        else:
            messages.error(request, (
                f'Failed to edit {item.name}. '
                f'Please check the form for validity.'
            ))
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


@login_required
def delete_merch(request, merch_id):
    """
    Allow superuser to delete merchandise in store
    """

    if not request.user.is_superuser:
        messages.error(request, "Only store owners are permitted to do that")
        return redirect(reverse('home'))

    if request.user.is_superuser:
        item = get_object_or_404(Merch, pk=merch_id)
        item.delete()
        messages.success(request, 'Merchandise has been deleted!')

    return redirect(reverse('merchandise'))
