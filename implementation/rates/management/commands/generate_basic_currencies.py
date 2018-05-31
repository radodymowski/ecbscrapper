# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

# TODO zamiast generować waluty można by np. scrappować je z listy linków z
# TODO https://www.ecb.europa.eu/home/html/rss.en.html
from rates.models import Currency


class Command(BaseCommand):
    help = 'Skrypt do wygenerowania zestawu walut w bazie'

    CURRENCIES = [
        {'name': 'US dollar', 'symbol': 'USD'},
        {'name': 'Japanese yen', 'symbol': 'JPY'},
        {'name': 'Bulgarian lev', 'symbol': 'BGN'},
        {'name': 'Czech koruna', 'symbol': 'CZK'},
        {'name': 'Danish krone', 'symbol': 'DKK'},
        {'name': 'Estonian kroon', 'symbol': 'EEK'},
        {'name': 'Pound sterling', 'symbol': 'GBP'},
        {'name': 'Hungarian forint', 'symbol': 'HUF'},
        {'name': 'Polish zloty', 'symbol': 'PLN'},
        {'name': 'Romanian leu', 'symbol': 'RON'},
        {'name': 'Swedish krona', 'symbol': 'SEK'},
    ]

    def handle(self, *args, **options):
        for data_dict in self.CURRENCIES:
            Currency.objects.get_or_create(**data_dict)
