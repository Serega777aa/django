from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = '<h1>Главная</h1>'
    logger.info('Visited home page')
    return HttpResponse(html)


def about(request):
    html = '<h1>О себе</h1>'
    logger.info('Visited about page')
    return HttpResponse(html)
