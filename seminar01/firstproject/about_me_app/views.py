from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    context = {"title": "Главная страница", "content": "Моя первая HTML станица"}
    logger.info(f'Page index.html loaded')
    return render(request, template_name='about_me_app/index.html', context=context)


def about(request):
    context = {"title": "Обо мне", "content": "Обо мне"}
    logger.info(f'Page about.html loaded')
    return render(request, template_name='about_me_app/about.html', context=context)


def form(request):
    context = {"title": "Заявка", "content": "Оставить заявку"}
    logger.info(f'Page form.html loaded')
    return render(request, template_name='about_me_app/form.html', context=context)
