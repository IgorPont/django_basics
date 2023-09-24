from django.urls import path
from . import views

urlpatterns = [
    path('coinplay/<int:count>/', views.coin, name='coinplay'),
    path('diceplay/<int:count>/', views.dice, name='diceplay'),
    path('randomizer/<int:count>/', views.random_number, name='random_number'),
    path('get_a_game/', views.simple_games_forms, name='simple_games_forms'),

]
