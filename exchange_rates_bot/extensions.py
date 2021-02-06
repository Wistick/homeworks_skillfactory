from config import rates
import requests
import json


class ExchangeAPI:
    @staticmethod
    def get_rate(base, quote, amount):
        if quote == base:
            raise APIException(f'Нельзя перевести одинаковые валюты {quote.upper()}.')

        try:
            rates[quote] = rates[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote.upper()}.')

        try:
            rates[base] = rates[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base.upper()}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount.lower()}".')

        response = requests.get(f'https://api.exchangeratesapi.io/latest?base={rates[base]}&symbols={rates[quote]}')
        convert = json.loads(response.content)
        exchange_rate = convert['rates'][rates[quote]]
        result = float(amount) * exchange_rate
        result = format(result, '.2f')
        return result


class APIException(Exception):
    pass
