# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Currency(models.Model):
    """
    model of currency with name and shortened symbol name
    """
    name = models.CharField(max_length=100, verbose_name=u'name')
    symbol = models.CharField(max_length=3, verbose_name=u'symbol')

    class Meta:
        verbose_name = u'Currency'
        verbose_name_plural = u'Currencies'

    def __str__(self):
        return u'{} ({})'.format(self.name, self.symbol)


class ExchangeRate(models.Model):
    """
    model of daily exchange rate: 1 EUR to related currency
    """
    currency = models.ForeignKey(Currency, verbose_name=u'currency')

    euro_rate = models.FloatField(verbose_name=u'1 euro rate')
    date = models.DateField(verbose_name=u'date')

    class Meta:
        verbose_name = u'exchange rate'
        verbose_name_plural = u'exchange rates'

    def __str__(self):
        return u'1 EUR = {} {} ({})'.format(self.euro_rate, self.currency.symbol, self.date)
