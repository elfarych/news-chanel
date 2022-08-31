import requests
from . import models
from datetime import datetime
from . import tg_sender


token = 'cl4uwk0goc1tqgfcudh7gxsqcsjb9cj71fnqd3pf'
base_url = 'https://cryptonews-api.com/api/v1'


def get_news():
    url = base_url + f'/category?section=alltickers&items=100&page=1&token={token}'
    r = requests.get(url)
    data = r.json()
    news = data['data']

    for n in news:
        try:
            tickers = ''
            for i in n['tickers']:
                tickers = tickers + f'#{i} '
            if n['image_url']:
                post = models.Post.objects.create(
                    title=n['title'],
                    text=n['text'],
                    image=n['image_url'],
                    source_name=n['source_name'],
                    source_url=n['news_url'],
                    post_date=n['date'],
                    sentiment=n['sentiment'],
                    tickers=tickers
                )
                post.save()

        except:
            continue


def check_news_tg_sent():
    news = models.Post.objects.filter(tg_sent=False)
    for post in news:
        tg_sender.send_telegram_news_message(post)
        post.tg_sent = True
        post.save()

