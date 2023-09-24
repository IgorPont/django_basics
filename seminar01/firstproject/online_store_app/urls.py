from django.urls import path
from . import views
from .views import ProductCreate

urlpatterns = [
    path('orders/<int:client_id>/', views.get_orders_by_client, name='get_orders_by_client'),
    path('orders/', views.order_list, name='order_list'),
    path('products_list/', views.get_products_all, name='get_products_all'),
    path('product_create/', ProductCreate.as_view())
]
