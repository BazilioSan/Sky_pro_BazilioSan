import os
import logging
import configparser

from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date

from src.utils import get_transaction_from_csv, get_transaction_from_xlsx, get_transactions_json

from src.wiget import extraction_date, mask_of_data

from src.sorting import sorting_transactions_by_description
from src.sorting import counting_categories

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
        return get_transactions_json(file_path)
    elif user_choice == "2":
        print("Для обработки выбран CSV-файл.")
        file_path = config.get('paths', 'csv_file')
        return get_transaction_from_csv(file_path)
    elif user_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        file_path = config.get('paths', 'xlsx_file')
        return get_transaction_from_xlsx(file_path)
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

    while True:
        sort_order = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if sort_order in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")

    if sort_order == "да":
        while True:
            user_choice_for_date_sort = input("Отсортировать по возрастанию или убыванию? (введите В или У)").upper()
            if user_choice_for_date_sort in ["В", "У"]:
                break
            print("Введён некорректный ответ. Повторите ввод ответа.")
        if user_choice_for_date_sort == "В":
            order = True
        elif user_choice_for_date_sort == "У":
            order = False

        transactions_sorted_by_date = sort_by_date(filtered_transactions, order)

    elif sort_order == "нет":
        transactions_sorted_by_date = filtered_transactions

    # if sort_order == "да":
    #     sort_direction = input("Отсортировать по возрастанию или по убыванию? ").lower()
    #     if sort_direction == "возрастанию":
    #         # sort_by_date(filtered_transactions, order=True)
    #         order = True
    #     elif sort_direction == "убыванию":
    #         # sort_by_date(filtered_transactions, order=False)
    #         order = False
    #     else:
    #         print("Неверный ввод. Сортировка не выполнена.")
    #         return []

    filter_currency = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if filter_currency == "да":
        # filter_by_currency(filtered_transactions, "RUB")
        rub_transactions = [
            transaction for transaction in transactions_sorted_by_date if transaction["currency_code"] == "RUB"
        ]
    elif filter_currency == "нет":
        rub_transactions = transactions_sorted_by_date

    filter_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if filter_description == "да":
        search_string = input("Введите слово для поиска в описании: ")
        sorted_by_description = sorting_transactions_by_description(rub_transactions, search_string)
        filtered_transactions = sorted_by_description

    return filtered_transactions


def display_transactions(transactions):
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации.")
        return

    print("Всего банковских операций в выборке:", len(transactions))

    for transaction in transactions:
        print(f"{extraction_date(transaction['date'])}, {transaction['description']}")
        if transaction['description'] != "Открытие вклада":
            print(f"{mask_of_data(transaction.get('from', ' '))} -> {mask_of_data(transaction['to'])}")
        else:
            print(f"Открытие вклада на  -> {mask_of_data(transaction['to'])}")

        print(f"Сумма: {transaction.get('amount')}, {transaction.get('currency_name')}")

        print("-" * 50)


def main():
    logger.info(f"Запуск функции")
    transactions = read_transactions()
    filtered_transactions = filter_and_sort_transactions(transactions)
    display_transactions(filtered_transactions)


if __name__ == "__main__":
    main()
