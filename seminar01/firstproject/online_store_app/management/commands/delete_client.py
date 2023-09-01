from django.core.management.base import BaseCommand
from online_store_app.models import Client


class Command(BaseCommand):
    help = 'Delete client by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client to delete ID.')

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client:
            client.delete()
        self.stdout.write(f'{client} delete')
