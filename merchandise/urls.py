from django.urls import path
from . import views



urlpatterns = [
    path('', views.merchandise, name='merchandise'),
    path('specials/', views.specials, name='specials'),
    path('details/<int:merch_id>/', views.details, name='merch_details'),
    path('add/', views.add_merch, name='add_merch'),
    path('edit/<int:merch_id>/', views.edit_merch, name='edit_merch'),
]