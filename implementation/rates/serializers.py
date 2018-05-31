from rest_framework.serializers import ModelSerializer

from rates.models import ExchangeRate, Currency


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class ExchangeRateSerializer(ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('currency', 'euro_rate', 'date')
