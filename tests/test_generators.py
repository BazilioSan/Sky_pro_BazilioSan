from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(fxtr_for_generators):
    """Функция тестирования filter_by_currency"""

    transactions = fxtr_for_generators
    usd_transactions = filter_by_currency(transactions, "USD")

    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_transaction_descriptions(fxtr_for_generators):
    """Функция тестирования transaction_descriptions"""

    transactions = fxtr_for_generators
    descriptions = transaction_descriptions(transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator() -> None:
    """Функция тестирования card_number_generator"""

    card_num = card_number_generator(48, 50)

    assert next(card_num) == "0000 0000 0000 0048"
    assert next(card_num) == "0000 0000 0000 0049"
    assert next(card_num) == "0000 0000 0000 0050"
