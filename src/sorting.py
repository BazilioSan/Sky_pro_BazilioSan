import re
from collections import Counter
from typing import Dict, List

data = [
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
]


def sorting_transactions_by_description(transactions, search_string: str) -> List[Dict]:
    """Функция принимает список транзакций (словарей) и слово для сортировки.
    Возвращает список транзакций (словарей), у которых в описании есть указанное слово."""
    pattern = rf"{search_string}"
    result_transactions_dict = [
        transaction
        for transaction in transactions
        if re.findall(pattern, transaction["description"], flags=re.IGNORECASE)
    ]
    return result_transactions_dict


def counting_categories(transactions: List[Dict], categories: List[str]) -> Dict:
    """Функция принимает список транзакций (словарей) и категории (список).
    Возвращает словарь вида категория: количество операций."""
    category_list = []
    for transaction in transactions:
        for category in categories:
            pattern = rf"{category}"
            if re.findall(pattern, transaction["description"], flags=re.IGNORECASE):
                category_list.append(transaction["description"])
    result_category_dict = Counter(category_list)
    return dict(result_category_dict)


if __name__ == "__main__":
    print(sorting_transactions_by_description(data, "карт"))
    print()
    print(counting_categorys(data, ["перевод с карты", "перевод Организации"]))
