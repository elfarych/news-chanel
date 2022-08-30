from django.db import models
from django.db.models import Model


class Coin(models.Model):
    coin_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    rank = models.PositiveSmallIntegerField(null=True)
    symbol = models.CharField(max_length=15, null=True)
    fullname = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('rank',)

    def __str__(self):
        return f'{self.name} - {self.symbol}'


class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.SET_NULL, null=True, related_name='events')
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')
    event_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, max_length=2000)
    event_date = models.DateTimeField()
    proof = models.CharField(null=True, max_length=255)
    source = models.CharField(null=True, max_length=255)
    tg_sent = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-event_date',)

    def __str__(self):
        return f'{self.title} - {self.coin}'


class Post(models.Model):
    title = models.CharField(unique=True, max_length=255)
    text = models.TextField(null=True)
    image = models.CharField(max_length=255)
    source_name = models.CharField(max_length=150)
    source_url = models.CharField(max_length=200)
    post_date = models.CharField(null=True, blank=True, max_length=150)
    tickers = models.CharField(max_length=50)
    sentiment = models.CharField(max_length=50)
    tg_sent = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

