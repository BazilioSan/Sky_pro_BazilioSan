from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.search import categorize_transactions
from src.utils import get_transaction_from_csv, get_transaction_from_xlsx, get_transactions_json
from src.wiget import extraction_date, mask_of_data


def main():
    global filtered_transactions

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = get_transactions_json("transactions.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = get_transaction_from_csv("transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = get_transaction_from_xlsx("transactions.xlsx")
    else:
        print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
        return

    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. "
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
    ).upper()
    if status in ["EXECUTED", "CANCELED", "PENDING"]:
        filtered_transactions = filter_by_state(transactions, status)
    else:
        print(f"Статус операции '{status}' недоступен.")

    sort_order = input("Отсортировать операции по дате? Да/Нет: ").lower()

    if sort_order == "да":
        sort_direction = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if sort_direction == "возрастанию":
            sort_by_date(list_of_dicts=filtered_transactions, order=True)
        elif sort_direction == "убыванию":
            sort_by_date(list_of_dicts=filtered_transactions, order=False)
        else:
            print("Неверный ввод. Сортировка не выполнена.")
            return

    filter_currency = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if filter_currency == "да":
        filter_by_currency(filtered_transactions, "RUB")

    filter_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if filter_description == "да":
        search_term = input("Введите слово для поиска в описании: ")
        transaction_descriptions(filtered_transactions, search_term)

    print("Всего банковских операций в выборке:", len(filtered_transactions))

    for transaction in filtered_transactions:

        if not filtered_transactions:
            print("Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации.")
            return

        print(f"{extraction_date('date')}, {transaction['description']}")
        print(mask_of_data(transaction))
        print(f"Сумма: {transaction['amount']} {transaction['currency']}") # тут как то надо впихать значения из categorize_transactions


if __name__ == "__main__":
    main()
