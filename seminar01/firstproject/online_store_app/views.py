from django.shortcuts import render, get_object_or_404
from online_store_app.models import Client, Product, Order
from online_store_app.forms import ProductForm
from django.views.generic import CreateView


def get_orders_by_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    order = Order.objects.filter(order_client=client_id)

    context = {
        'title': 'Заказы клиента',
        'client': client,
        'orders': order,
    }
    return render(request, template_name='online_store_app/orders.html', context=context)


def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, template_name='online_store_app/order_list.html', context=context)


def get_products_all(request):
    """Get a list of all products"""
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, template_name='online_store_app/product_list.html', context=context)


# Попробуем через класс
class ProductCreate(CreateView):
    # Модель куда выполняется сохранение
    model = Product
    # Класс, на основе которого будет валидация полей
    form_class = ProductForm
    # Выведем все существующие записи на странице
    extra_context = {'products': Product.objects.all()}
    # Шаблон, с помощью которого будут выводиться данные
    template_name = 'product_create.html'
    # На какую страницу будет перенаправление в случае успешного сохранения формы
    success_url = '/product_list/'
