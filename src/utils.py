import csv
import json
import logging
import os
from typing import Union, Any

import pandas as pd

from src.external_api import convert_currency

logs_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_json(file_path: str = None) -> list:
    """Функция чтения и парсинга файла с транзакциями"""

    logger.info(f"Запуск функции. Чтение файла {file_path}")

    if file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, ".." "data", "operations.json")

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


def get_transaction_amount(transactions: list, transaction_id: int) -> Union[str, Any]:
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


def get_transaction_from_csv(file_path: str = None) -> list:
    """Функция чтения и парсинга файла с транзакциями из CSV"""

    if file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "data", "transactions.csv")

    logger.info(f"Запуск функции. Чтение файла из директории {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = csv.reader(file, delimiter=";")
            next(data)  # пропускаем заголовок

            transactions = []
            for row in data:
                transaction = {
                    "id": row[0],
                    "state": row[1],
                    "date": row[2],
                    "amount": row[3],
                    "currency_name": row[4],
                    "currency_code": row[5],
                    "from": row[6],
                    "to": row[7],
                    "description": row[8]
                }
                transactions.append(transaction)

            if not transactions:
                logger.error("Ошибка. Файл не содержит данных")
                raise ValueError("Файл не содержит данные")

            logger.info("Функция успешно отработала.")
            return transactions

    except FileNotFoundError:
        logger.error("Ошибка. Файл не найден")
        print("Ошибка. Файл не найден")
        return []


def get_transaction_from_xlsx(file_path: str = None) -> list[dict]:
    """Функция чтения и парсинга файла с транзакциями из XLSX"""

    if file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "data", "transactions.xlsx")

    logger.info(f"Запуск функции. Чтение файла из директории {file_path}")
    try:
        data = pd.read_excel(file_path)
        rows = data.to_dict("records")
        if not rows:
            logger.error("Ошибка. Файл не содержит данных")
            raise ValueError("Файл не содержит данные")
        return rows

    except FileNotFoundError:
        logger.error("Ошибка. Файл не найден")
        print("Ошибка. Файл не найден")
        return []
