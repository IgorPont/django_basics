from django.urls import path
from . import views

urlpatterns = [
    path('coinplay/<int:count>/', views.coin, name='coinplay'),
    path('diceplay/<int:count>/', views.dice, name='diceplay'),
    path('randomizer/<int:count>/', views.random_number, name='random_number'),

]
