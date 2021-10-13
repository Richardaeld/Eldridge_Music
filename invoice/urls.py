from django.urls import path
from . import views


urlpatterns = [
    # path('special/<special_id>/<lesson_subscription>', views.checkout_special, name='checkout_special'),
    path('lesson/<lesson_id>/<lesson_subscription>', views.checkout_lesson, name='checkout_lesson')
]