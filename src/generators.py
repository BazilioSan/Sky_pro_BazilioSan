from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[str, None, None]:
    """Функция, возвращающая генератор номеров транзакций (id) с указанной валютой."""

    return (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )


def transaction_descriptions(transactions: dict) -> Generator[str, None, None]:
    """Функция, возвращающая генератор описаний транзакций"""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция-генератор номеров карт"""

    for num in range(start, end + 1):
        card_number = (16 - len(str(num))) * "0" + str(num)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
