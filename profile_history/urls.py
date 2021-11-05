from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('invoice_history/<invoice_number>', views.invoice_history, name='invoice_history'),
]