from django.core.management.base import BaseCommand
from online_store_app.models import Client


class Command(BaseCommand):
    """Обновление по имени клиента"""
    help = 'Update client by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID.')
        parser.add_argument('new_name', type=str, help='New client name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_name = kwargs.get('new_name')
        client_name = Client.objects.filter(pk=pk).first()
        client_name.client_name = new_name
        client_name.save()
        self.stdout.write(f'{client_name}')
