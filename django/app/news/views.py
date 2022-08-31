from django.http import HttpResponse
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
import time

from . import models
from . import serializers
from . import service
from . import news
from . import tg_sender


class CoinListView(generics.ListAPIView):
    serializer_class = serializers.CoinSerializer
    queryset = models.Coin.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class EventListView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = service.EventsFilter


class PostListView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()


def update_data(request):
    tg_sender.send_report()
    service.get_events()
    news.get_news()
    time.sleep(5)
    send_data_to_tg()

    time.sleep(600)
    update_data(request)
    return HttpResponse(f'Data updated...')


def send_data_to_tg():
    news.check_news_tg_sent()
    service.check_events_tg_sent()
    return HttpResponse(f'Sent to Telegram...')


def add_coins(request):
    service.create_coins()
    return HttpResponse(f'Coins created')


def delete_coins(request):
    service.delete_coins()
    return HttpResponse(f'All coins deleted')


def update_coins(request):
    service.update_coins()
    return HttpResponse(f'All coins updated')


def add_categories(request):
    service.create_categories()
    return HttpResponse(f'All categories created')

