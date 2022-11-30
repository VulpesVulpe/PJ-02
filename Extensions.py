import requests
import json
from Config import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена!")

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            amount = float(amount.replace(",","."))
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        resp = json.loads(r.content)
        new_price = resp[base_ticker] * amount
        new_price = round(new_price, 3)
        message = f"Цена {amount} {quote} в {base} : {new_price}"

        return message


