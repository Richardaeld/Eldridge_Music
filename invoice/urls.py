from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.invoice, name='invoice'),
    path(
        'checkout_success/<invoice_number>',
        views.checkout_success, name='checkout_success'
    ),
    path('wh/', webhook, name='webhook'),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data, name='cache_checkout_data'
    )
]
