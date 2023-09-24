import random

from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from gamesapp.forms import ChooseGameForm
import logging

logger = logging.getLogger(__name__)


def coin(request, count):
    try:
        side = [random.choice(['avers', 'revers']) for _ in range(count)]
    except IndexError as exc:
        logger.exception(f'Error occurred: {exc}')
        return HttpResponse(f"Coin lost")
    else:
        context = {"title": "Монетка", "attempts": side}
        logger.info(f'coinplay requested; Coin side: {side}')
        return render(request, template_name='gamesapp/games.html', context=context)


def dice(request, count):
    cube_side = [randint(1, 6) for _ in range(count)]
    context = {"title": "Кубик", "attempts": cube_side}
    logger.info(f'diceplay requested; Cube side: {cube_side}')
    return render(request, template_name='gamesapp/games.html', context=context)


def random_number(request, count):
    answer = [randint(0, 100) for _ in range(count)]
    context = {"title": "Рандомное число", "attempts": answer}
    logger.info(f'randomizer requested; Random number: {answer}')
    return render(request, template_name='gamesapp/games.html', context=context)


def simple_games_forms(request):
    coin_sides = ('obverse', 'reverse')
    if request.method == 'POST':
        form = ChooseGameForm(request.POST)
        title = ['Coin play', 'Dice', 'Rundom namber'][int(form.data['a_game'])]
        if form.is_valid():
            if title == 'Coin play':
                attempts_pack = [coin_sides[randint(0, 1)] for _ in range(form.cleaned_data['attempts'])]
            elif title == 'Dice':
                attempts_pack = [randint(1, 6) for _ in range(form.cleaned_data['attempts'])]
            else:
                attempts_pack = [randint(0, 99) for _ in range(form.cleaned_data['attempts'])]
            logger.info(f'Sending results for game {title}')
            return render(request,
                          'gamesapp/common_records.html',
                          {
                              'title': title,
                              'attempts': attempts_pack
                          })
    else:
        form = ChooseGameForm()
        logger.info('Sending game chooser')
        return render(request, 'gamesapp/choose_game_form.html', {'form': form, 'title': 'Choose game'})
