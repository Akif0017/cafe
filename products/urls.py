from django.urls import path 
from .views import index, coffees, croissants, our_menu

urlpatterns = [
    path('', index, name='home'),
    path('coffees/', coffees, name='coffees'),
    path('croissants/', croissants, name='croissants'),
    path('our_menu/', our_menu, name='our_menu'),
]