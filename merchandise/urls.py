from django.urls import path
from . import views



urlpatterns = [
    path('', views.merchandise, name='merchandise'),
    path('specials/', views.specials, name='specials'),
    path('details/<merch_id>', views.details, name='merch_details')
]