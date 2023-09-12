import random

from django.shortcuts import render
from django.http import HttpResponse
from random import randint
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


