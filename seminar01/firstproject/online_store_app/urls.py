from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:client_id>/', views.get_orders_by_client, name='get_orders_by_client'),
    path('orders/', views.order_list, name='order_list'),
]
