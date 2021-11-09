from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from merchandise.models import Merch


def cart_contents(request):
    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, amount in cart.items():
        item = get_object_or_404(Merch, pk=item_id)
        total += amount * item.price
        item_count += amount
        cart_items.append({
            'item_id': item_id,
            'amount': amount,
            'item': item,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'FREE_DELIVERY_THRESHOLD': settings.FREE_DELIVERY_THRESHOLD,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }

    return context
