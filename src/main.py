import os
import logging
import configparser

from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date

from src.utils import get_transaction_from_csv, get_transaction_from_xlsx, get_transactions_json
from src.wiget import extraction_date, mask_of_data

config = configparser.ConfigParser()
config.read('config.ini')

logs_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(logs_dir, exist_ok=True)

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(os.path.join(logs_dir, "main.log"), encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_choice = input("Ваш выбор: ")
    logger.info(f"Выбран пункт {user_choice}")

    if user_choice == "1":
        print("Для обработки выбран JSON-файл.")
        file_path = config.get('paths', 'json_file')
        return get_transactions_json(file_path), user_choice
    elif user_choice == "2":
        print("Для обработки выбран CSV-файл.")
        file_path = config.get('paths', 'csv_file')
        return get_transaction_from_csv(file_path), user_choice
    elif user_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        file_path = config.get('paths', 'xlsx_file')
        return get_transaction_from_xlsx(file_path), user_choice
    else:
        print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
        return [], None


def filter_and_sort_transactions(transactions):
    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. "
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
    ).upper()
    if status in ["EXECUTED", "CANCELED", "PENDING"]:
        filtered_transactions = filter_by_state(transactions, status)
    else:
        print(f"Статус операции '{status}' недоступен.")
        return []

    sort_order = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_order == "да":
        sort_direction = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if sort_direction == "возрастанию":
            sort_by_date(filtered_transactions, order=True)
        elif sort_direction == "убыванию":
            sort_by_date(filtered_transactions, order=False)
        else:
            print("Неверный ввод. Сортировка не выполнена.")
            return []

    filter_currency = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if filter_currency == "да":
        filter_by_currency(filtered_transactions, "RUB")

    filter_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if filter_description == "да":
        search_term = input("Введите слово для поиска в описании: ")
        transaction_descriptions(filtered_transactions, search_term)

    return filtered_transactions


def display_transactions(transactions, user_choice):
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации.")
        return

    print("Всего банковских операций в выборке:", len(transactions))

    for transaction in transactions:
        print(f"{extraction_date(transaction['date'])}, {transaction['description']}")
        print(f"{mask_of_data(transaction.get('from', ' '))} -> {mask_of_data(transaction['to'])}")

        # if transaction['operationAmount'] in transactions:
        #     print(f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']}")
        # else:
        #     print(f"Сумма: {transaction['amount']} {transaction['currency']}")

        # if user_choice == "1":
        #     print(f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']}")
        # else:
        #     print(f"Сумма: {transaction['amount']} {transaction['currency']}")

        if transaction['from'] != None and transaction['to'] != None:
            print(f"{transaction['from']} -> {transaction['to']}")
            print(f"Сумма: {transaction['operationAmount'].get('amount')}")
        else:
            print(f"{transaction['to']}")
            print(f"Сумма: {transaction['operationAmount'].get('amount')}
            " {transaction['operationAmount']['currency'].get('name')}")

            print("-" * 50)


def main(user_choice):
    logger.info(f"Запуск функции")
    transactions = read_transactions()
    filtered_transactions = filter_and_sort_transactions(transactions)
    display_transactions(filtered_transactions, user_choice)


if __name__ == "__main__":
    main()
