from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from merchandise.models import Merch

def shopping_bag(request):

    template = 'shopping_bag/shopping_bag.html'

    return render(request, template)

def add_to_cart(request, item_id):

    amount = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += amount
    else:
        cart[item_id] = amount

    request.session['cart'] = cart

    item  = get_object_or_404(Merch, pk=item_id)

    messages.success(request, item.name + " was added to cart")

    return redirect(redirect_url)


def adjust_cart(request, item_id):

    amount = int(request.POST.get('amount'))
    cart = request.session.get('cart', {})

    if amount > 0:
        cart[item_id] = amount
    else:
        cart.pop(item_id)

    request.session['cart'] = cart

    # item  = get_object_or_404(Merch, pk=item_id)

    # messages.success(request, item.name + " was added to cart")

    return redirect(reverse('shopping_bag'))


def remove_cart_item(request, item_id):

    cart = request.session.get('cart', {})

    cart.pop(item_id)

    request.session['cart'] = cart

    # item  = get_object_or_404(Merch, pk=item_id)

    # messages.success(request, item.name + " was added to cart")

    return redirect(reverse('shopping_bag'))