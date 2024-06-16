from typing import Dict, Generator, List, Union

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions: List[Dict[str, Union[int, str, dict[str, dict[str, str]]]]] = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_filter_by_currency() -> Union[Generator[Dict[str, int], None, None], Dict[str, int]]:
    """Функция тестирования filter_by_currency"""

    usd_transactions = filter_by_currency(transactions, "USD")
    for x in range(2):
        return next(usd_transactions)["id"]
    assert next(usd_transactions) == {"id": 939719570}
    assert next(usd_transactions) == {"id": 142264268}


def test_transaction_descriptions() -> Generator[str, None, None]:
    """Функция тестирования transaction_descriptions"""

    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        return next(descriptions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator() -> Generator[str, None, None]:
    """Функция тестирования card_number_generator"""

    card_num = card_number_generator(48, 50)
    for card_number in card_number_generator(48, 50):
        return card_number
    assert next(card_num) == "0000 0000 0000 0048"
    assert next(card_num) == "0000 0000 0000 0049"
    assert next(card_num) == "0000 0000 0000 0050"
