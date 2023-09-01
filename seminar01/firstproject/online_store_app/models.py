from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=100)
    client_phone_number = models.CharField(max_length=30)
    client_address = models.TextField()
    client_reg_date = models.DateField()

    def __str__(self):
        return f'{self.client_name}: зарегистрирован - {self.client_reg_date}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    product_addition_date = models.DateField()

    def __str__(self):
        return f'{self.product_name}: цена - {self.product_price}'


class Order(models.Model):
    order_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_product = models.ManyToManyField(Product)
    order_total_amount = models.FloatField()
    order_placement_date = models.DateField()

    def __str__(self):
        return f'Общая сумма заказа: {self.order_total_amount}, дата оформления: {self.order_placement_date}'
