import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()
api_key = os.getenv("API_KEY")


def convert_currency(transaction_convert: dict):
    """Функция конвертации валюты через курс внешнего API"""

    amount = transaction_convert["amount"]
    currency = transaction_convert["currency"]

    try:
        if currency == "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
        elif currency == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
    except RequestException:
        return 0
