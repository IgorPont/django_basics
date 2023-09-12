from django.shortcuts import render, get_object_or_404
from online_store_app.models import Client, Product, Order


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
