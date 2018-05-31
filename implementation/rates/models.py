# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'nazwa')
    symbol = models.CharField(max_length=3, verbose_name=u'symbol')

    class Meta:
        verbose_name = u'Waluta'
        verbose_name_plural = u'Waluty'

    def __str__(self):
        return u'{} ({})'.format(self.name, self.symbol)


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, verbose_name=u'waluta')

    euro_rate = models.FloatField(verbose_name=u'kurs za 1 euro')
    date = models.DateField(verbose_name=u'data')

    class Meta:
        verbose_name = u'kurs wymiany'
        verbose_name_plural = u'kursy wymiany'

    def __str__(self):
        return u'1 EUR = {} {} ({})'.format(self.euro_rate, self.currency.symbol, self.date)
