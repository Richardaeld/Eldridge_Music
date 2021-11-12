from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages

from django.conf import settings
from merchandise.models import Merch


def shopping_bag(request):
    MEDIA_URL = settings.MEDIA_URL
    template = 'shopping_bag/shopping_bag.html'
    context = {
        'MEDIA_URL': MEDIA_URL,
    }
    return render(request, template, context)


def add_to_cart(request, item_id):
    amount = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    item = get_object_or_404(Merch, pk=item_id)

    if item_id in list(cart.keys()):
        cart[item_id] += amount
        messages.success(
            request, f'{item.name}\'s quantity is now {cart[item_id]}')
    else:
        cart[item_id] = amount
        messages.success(request, f'({amount}) - {item.name} added to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    item = get_object_or_404(Merch, pk=item_id)
    amount = int(request.POST.get('amount'))
    cart = request.session.get('cart', {})

    if amount > 0:
        cart[item_id] = amount
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    messages.success(request, f'{item.name}\'s quantity is now {amount}')
    return redirect(reverse('shopping_bag'))


def remove_cart_item(request, item_id):
    try:
        item = get_object_or_404(Merch, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        messages.success(request, f'{item.name} was removed from cart')
    except Exception as e:
        messages.error(request, (
            f'Error occured: '
            f'{e} while removing {item.name} try again later'
        ))
    return redirect(reverse('shopping_bag'))
