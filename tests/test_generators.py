from typing import Dict, Union

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(fxtr_for_generators: Dict[str, Union[int, str]]) -> None:
    """
    Функция тестирования filter_by_currency
    """
    usd_transactions = filter_by_currency(fxtr_for_generators, "USD")

    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_transaction_descriptions(fxtr_for_generators: Dict[str, int]) -> None:
    """
    Функция тестирования transaction_descriptions
    """

    transactions = fxtr_for_generators
    descriptions = transaction_descriptions(transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


@pytest.mark.parametrize(
    "start, end, expected_output",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (0, 2, ["0000 0000 0000 0000", "0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
        (100125445786, 100125445788, ["0000 1001 2544 5786", "0000 1001 2544 5787", "0000 1001 2544 5788"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected_output: list[str]) -> None:
    """
    Функция тестирования card_number_generator
    """
    result = list(card_number_generator(start, end))
    assert result == expected_output
