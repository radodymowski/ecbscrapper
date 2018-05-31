# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from rates.scrapper import rate_scrapper


class Command(BaseCommand):
    help = 'Skrypt do uruchomienia scrappera walut'

    def handle(self, *args, **options):
        rate_scrapper()
