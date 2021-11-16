from django.urls import path
from . import views


urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('adjust_cart/<item_id>', views.adjust_cart, name='adjust_cart'),
    path(
        'remove_cart_item/<item_id>',
        views.remove_cart_item, name='remove_cart_item'
    )
]
