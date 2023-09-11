from django.urls import path
from . import views

urlpatterns = [
    path('001/', views.index, name='index'),
]
