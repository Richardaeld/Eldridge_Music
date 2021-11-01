from django.shortcuts import render, redirect, get_object_or_404
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