from django.urls import path
from . import views


urlpatterns = [
    path('', views.invoice, name='invoice')
    # path('special/<special_id>/<lesson_subscription>', views.checkout_special, name='checkout_special'),
    # path('lesson/<lesson_id>/<lesson_sku>', views.checkout_lesson, name='checkout_lesson'),
    # path('lesson-chechout/<sku>/<item_pk>', views.record_invoice, name='record_invoice')
]