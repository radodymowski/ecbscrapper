from rest_framework.serializers import ModelSerializer

from rates.models import ExchangeRate, Currency


class CurrencySerializer(ModelSerializer):
    """
    Currency serializer
    """
    class Meta:
        model = Currency
        fields = '__all__'


class ExchangeRateSerializer(ModelSerializer):
    """
    Exchange rate serializer (id field excluded, not needed propably)
    """
    class Meta:
        model = ExchangeRate
        fields = ('currency', 'euro_rate', 'date')
