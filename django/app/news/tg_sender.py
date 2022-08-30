import requests
import telebot

bot = telebot.TeleBot('5336001310:AAEAEJXYqk9yRuiIZ8DDe_HPRqDla2DPAzg')
chat_id = '-1001672957008'


def send_telegram_event_message(event):
    try:
        if event.coin:
            coin = event.coin
            text = f'#EVENTS\n\n' \
                   f'**Coin:** #{coin.symbol} | {coin.name}\n' \
                   f'**Event:** {event.title}\n' \
                   f'**Event date:** {event.event_date.strftime("%d-%m-%Y")}\n\n' \
                   f'[Source]({event.source})  |  [Coin on Coinmarketcap](https://coinmarketcap.com/currencies/{coin.coin_id}/)\n\n' \
                   f'All events on [Bitman events](https://bitman.trade/#/events)'

            if event.proof:
                r = requests.get(event.proof)
                bot.send_photo(chat_id, r.content, caption=text, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, text=text)
    except:
        return


def send_telegram_news_message(post):
    try:
        r = requests.get(post.image)
        text = f'#NEWS\n\n' \
               f'**{post.title}**\n' \
               f'{post.text}\n\n' \
               f'**Coin**: {post.tickers}\n' \
               f'**Sentiment:** {post.sentiment}\n' \
               f'**Source:** [{post.source_name}]({post.source_url})\n\n' \
               f'All news on [Bitman news](https://bitman.trade/#/news)'

        bot.send_photo(chat_id, r.content, caption=text, parse_mode="Markdown")
    except:
        return
