import pytest

from src.wiget import extraction_date, mask_of_data


@pytest.mark.parametrize(
    "data, expected_data",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("VISA 7965300734725465", "VISA 7965 30** **** 5465"),
        ("MSTR 7000792289606361", "MSTR 7000 79** **** 6361"),
        ("МИР 7158300734726758", "МИР 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Account 73654108430135871560", "Account **1560"),
        ("Acc 73654108430135871320", "Acc **1320"),
        ("MrCard 71583006758", "Ошибка при вводе данных")
    ],
)
def test_mask_of_data(data, expected_data):
    """Функция тестирования mask_of_data"""

    assert mask_of_data(data) == expected_data


@pytest.mark.parametrize(
    "date, expected_date", [("2018-07-11T02:26:18.671407", "11.07.2018"), ("2019-06-10T02:26:18.671407", "10.06.2019")]
)
def test_extraction_date(date, expected_date):
    """Функция тестирования extraction_date"""

    assert extraction_date(date) == expected_date
