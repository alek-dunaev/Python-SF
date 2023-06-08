import requests
import json
from config import keys

class APIException(Exception):
    pass

class СurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str,  amount: str):

        if quote == base:
            raise APIException('Невозможно перевести одинаковые валюты')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base} ')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker}&key=b9dbe2cb243fc8907b3869ecec332a89')
        total_base = json.loads(r.content)['data']
        text = round((float(total_base[f'{keys[quote]}{keys[base]}'])), 2)
        final_text = text * amount

        return final_text
