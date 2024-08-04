import pytest

from src.masks import get_account_mask, get_card_mask


@pytest.mark.parametrize(
    "card_num, expected_card_num",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (8000792289606361, "8000 79** **** 6361"),
        (9000792289607572, "9000 79** **** 7572"),
    ],
)
def test_get_card_mask(card_num: str, expected_card_num: str) -> bool:
    """Функция тестирования get_card_mask"""

    assert get_card_mask(card_num) == expected_card_num


@pytest.mark.parametrize(
    "account_num, expected_account_num",
    [(73654108430135874305, "**4305"), (73654108430135876549, "**6549"), (73654108430135877410, "**7410")],
)
def test_get_account_mask(account_num: str, expected_account_num: str) -> bool:
    """Функция тестирования get_account_mask"""

    assert get_account_mask(account_num) == expected_account_num
