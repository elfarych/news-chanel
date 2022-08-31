import requests
from . import models
from django_filters import rest_framework as filters
from . import tg_sender


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class EventsFilter(filters.FilterSet):
    categories = CharFilterInFilter(field_name='categories', lookup_expr='in')
    coin = CharFilterInFilter(field_name='coin', lookup_expr='in')

    class Meta:
        model = models.Event
        fields = ['categories', 'coin']


headers = {
    'x-api-key': "wZTN3WxqY41p2k9aucdeu7iLrtIiEq5c91WFS1OS",
    'Accept-Encoding': "deflate, gzip",
    'Accept': "application/json"
}
base_url = 'https://developers.coinmarketcal.com/v1'
coindar_url = 'https://coindar.org/api/v2/coins?access_token=65579:GsXyhnV7OgIASTuR5LA'


def delete_coins():
    coins = models.Coin.objects.all()
    for i in coins:
        i.delete()


def create_coins():
    url = base_url + '/coins'
    r = requests.get(url, headers=headers)
    r = r.json()
    coins = r['body']
    for i in coins:
        try:
            coin = models.Coin.objects.create(
                coin_id=i['id'],
                name=i['name'],
                rank=i['rank'],
                symbol=i['symbol'],
                fullname=i['fullname']
            )
            coin.save()
        except:
            continue


def update_coins():
    url = coindar_url
    coins = models.Coin.objects.all()
    r = requests.get(url, headers=headers)
    c_coins = r.json()

    for coin in coins:
        for c_coin in c_coins:
            try:
                c_name = c_coin['name'].lower()
                if c_name == coin.coin_id:
                    coin.image = c_coin['image_64'] or c_coin['image_32']
                    coin.save()
            except:
                continue


def create_events_by_page(page=1):
    url = base_url + f'/events?page={page}&max=75'
    r = requests.get(url, headers=headers)
    r = r.json()
    events = r['body']

    for i in events:
        coin = None
        category = None

        if len(i['categories']):
            i_category = i['categories'][0]
            try:
                category = models.Category.objects.get(category_id=i_category['id'])
            except:
                category = None

        if len(i['coins']):
            i_coin = i['coins'][0]
            try:
                coin = models.Coin.objects.get(coin_id=i_coin['id'])
            except:
                coin = None

        try:
            event = models.Event.objects.create(
                coin=coin,
                categories=category,
                event_id=i['id'],
                title=i['title']['en'],
                event_date=i['date_event'],
                proof=i['proof'],
                source=i['source']
            )
            event.save()
        except:
            continue


def get_events():
    for i in range(5):
        create_events_by_page(i)


def create_categories():
    url = base_url + '/categories'
    r = requests.get(url, headers=headers)
    r = r.json()
    categories = r['body']

    for i in categories:
        try:
            category = models.Category.objects.create(
                category_id=i['id'],
                name=i['name']
            )
            category.save()
        except:
            continue


def check_events_tg_sent():
    events = models.Event.objects.filter(tg_sent=False)
    for event in events:
        tg_sender.send_telegram_event_message(event)
        event.tg_sent = True
        event.save()

