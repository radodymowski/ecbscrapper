# -*- coding: utf-8 -*-
from datetime import date

import feedparser

from rates.models import Currency, ExchangeRate

FEED_URL_TEMPLATE = 'https://www.ecb.europa.eu/rss/fxref-<CURRENCY>.html'


def rate_scrapper():
    for currency in Currency.objects.all():
        parsed_feed = feedparser.parse(FEED_URL_TEMPLATE.replace('<CURRENCY>', currency.symbol.lower()))
        try:
            currency_rate = float(parsed_feed['entries'][0]['cb_exchangerate'].splitlines()[0])
            # TODO powinno się pobierać datę z danych RSS
            ExchangeRate.objects.get_or_create(currency=currency, euro_rate=currency_rate, date=date.today())
        except (KeyError, IndexError, ValueError):
            # przejdź do następnej iteracji jeżeli nie znaleziono właściwego klucza
            pass
