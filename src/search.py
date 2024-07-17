import re


def search_transactions(transactions: list, search_string: str) -> list:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка.
    """
    result = []
    for transaction in transactions:
        if re.search(search_string, transaction['description'], re.IGNORECASE):
            result.append(transaction)
    return result


def categorize_transactions(transactions: list, categories: str) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    category_counts: dict = {category: 0 for category in categories}
    for transaction in transactions:
        for category in categories:
            if re.search(category, transaction['description'], re.IGNORECASE):
                category_counts[category] += 1
                break
    return category_counts



