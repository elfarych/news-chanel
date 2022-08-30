from django.contrib import admin
from . import models


@admin.register(models.Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('rank', 'coin_id', 'name', 'fullname', 'symbol')
    search_fields = ('name', 'symbol', 'fullname')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'coin', 'tg_sent', 'event_date', 'date')
    search_fields = ('title', 'coin__name', 'coin__symbol')
    list_filter = ('tg_sent',)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tickers', 'tg_sent', 'date')
    search_fields = ('title', 'tickers')
    list_filter = ('tg_sent', 'tickers',)
