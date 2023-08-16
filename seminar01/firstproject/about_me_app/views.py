from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    logger.info(f'Page index.html loaded')
    return render(request, 'index.html')


def about(request):
    logger.info(f'Page about.html loaded')
    return render(request, 'info/about.html')


def form(request):
    logger.info(f'Page form.html loaded')
    return render(request, 'form.html')
