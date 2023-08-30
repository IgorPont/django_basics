from django.core.management.base import BaseCommand
from gamesapp.models import CoinPlay
from random import randint


class Command(BaseCommand):
    help = 'Thow a coin.'

    def handle(self, *args, **kwargs):
        CoinPlay.add_throws(randint(0, 1))
