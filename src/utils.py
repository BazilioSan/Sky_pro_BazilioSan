import json
import logging
import os

from src.external_api import convert_currency

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_json(file_path: str = None) -> list:
    """Функция чтения и парсинга файла с транзакциями"""

    logger.info(f"Запуск функции. Чтение файла {file_path}")

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
                logger.error("Ошибка. Файл не содержит список данных")
                raise ValueError("Файл не содержит список данных")

    except FileNotFoundError:
        logger.error("Ошибка. Файл не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка. Ошибка при чтении файла")
        raise ValueError("Ошибка при чтении файла")
    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        print(e)

        return []


def get_transaction_amount(transactions: list, transaction_id: int):
    """Функция конвертации конкретной транзакции"""

    logger.info(f"Запуск функции. Поиск транзакции с id {transaction_id}")
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
                    logger.info(f"Функция успешно отработала с результатом {rub_amount}")
                    return rub_amount
                else:
                    logger.error("Ошибка. Конвертация не совершена")
                    return "Конвертация не может быть выполнена"
    else:
        logger.error("Ошибка. Транзакция не найдена")
        return "Транзакция не найдена"

# if __name__ == "__main__":
#     transactions = get_transactions_json("../data/operations.json")
#     print(get_transaction_amount(transactions, 41428829))
