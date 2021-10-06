from django.urls import path
from . import views


urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('subscriptions/<sub_id>', views.subs_details, name='subs_details')
]