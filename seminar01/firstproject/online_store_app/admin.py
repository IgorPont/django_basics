from django.contrib import admin
from .models import Client, Product, Order


# вывод информации о клиентах на страницах списков
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'client_phone_number')
    ordering = ('client_name',)
    list_filter = ('client_name', 'client_phone_number')
    search_fields = ('client_name',)
    readonly_fields = ['client_reg_date', ]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client_name', 'client_phone_number', ],
            },
        ),
        (
            'Contacts',
            {
                'classes': ['collapse', ],
                'fields': ['client_email', 'client_address', ],
            },
        ),
        (
            'Reg',
            {
                'classes': ['collapse', ],
                'fields': ['client_reg_date', ],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_client', 'order_product', 'order_total_amount')
    ordering = ('order_client',)
    list_filter = ('order_client',)
    search_fields = ('order_client',)


# регистрируем модели в админке
admin.site.register(Client, ClientAdmin)
admin.site.register(Product)
admin.site.register(Order)
