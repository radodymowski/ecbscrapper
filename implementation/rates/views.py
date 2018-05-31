# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

from rates.models import ExchangeRate, Currency
from rates.serializers import ExchangeRateSerializer, CurrencySerializer


class CurrencyViewSet(ModelViewSet):
    """
    Currency viewset
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateViewSet(ModelViewSet):
    """
    Exchange rate viewset with records sorted by latest date
    """
    queryset = ExchangeRate.objects.order_by('-date')
    serializer_class = ExchangeRateSerializer
