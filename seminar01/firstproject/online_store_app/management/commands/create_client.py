from django.core.management.base import BaseCommand
from online_store_app.models import Client
from datetime import date
from random import randint


class Command(BaseCommand):
    help = 'Create fake clients.'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of fake clients.')

    def handle(self, *args, **options):
        amount = options.get('amount')
        for i in range(1, amount + 1):
            client = Client(
                client_name=f'Client Nm{i}',
                client_email=f'mail{i:0>4}@mail.com',
                client_phone_number=f'{randint(0, 9)}' * i,
                client_address=f'Adress Lorem ipsum ' * i,
                client_reg_date=date.today()
            )
            client.save()
