import json
import os

from utils.external_api import convert_currency


def get_transactions_json(file_path: str = None) -> list:
    """Функция чтения и парсинга файла с транзакциями"""

    if file_path is None:
        base_dir = os.getcwd()
        file_path = os.path.join(base_dir, "data", "operations.json")

    # Таким образом мы предусматриваем, что можно ввести путь до какого либо файла с данными,
    # а по дефолту будет файл из папки data

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data: list = json.load(file)
            if type(data) == list:
                return data
            else:
                raise ValueError("Файл не содержит список данных")

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("Ошибка при чтении файла")
    except ValueError as e:
        print(e)

        return []


def get_transaction_amount(transactions: list, transaction_id: int):
    """Функция конвертации конкретной транзакции"""

    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_currency(transaction_convert), 2)
                if rub_amount != 0:
                    return rub_amount
                else:
                    return "Конвертация не может быть выполнена"
    else:
        return "Транзакция не найдена"


# if __name__ == "__main__":
#     transactions = get_transactions_json("../data/operations.json")
#     print(get_transaction_amount(transactions, 41428829))
