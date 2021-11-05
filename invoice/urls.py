from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('checkout_success/<invoice_number>', views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data')
    # path('special/<special_id>/<lesson_subscription>', views.checkout_special, name='checkout_special'),
    # path('lesson/<lesson_id>/<lesson_sku>', views.checkout_lesson, name='checkout_lesson'),
    # path('lesson-chechout/<sku>/<item_pk>', views.record_invoice, name='record_invoice')
]