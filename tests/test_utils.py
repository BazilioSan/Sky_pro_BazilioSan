from pathlib import Path
from unittest.mock import patch

from src.utils import get_transaction_amount, get_transactions_json
from src.utils import get_transaction_from_csv, get_transaction_from_xlsx


def test_read_file_with_data():
    """Тест чтения из файла"""

    file_path = Path("data/operations.json")
    transactions = get_transactions_json(file_path)
    assert type(transactions) == list


def test_nonexistent_file():
    """Тест чтения из несуществующего файла"""

    nonexistent_file = "/nonexistent/file.json"
    transactions = get_transactions_json(nonexistent_file)
    assert transactions == []


def test_invalid_file():
    """Тест чтения из файла с невалидными данными"""

    invalid_file = Path("invalid_file.txt")
    with open(invalid_file, "w") as file:
        file.write("Invalid data")
    try:
        transactions = get_transactions_json(invalid_file)
        assert transactions == []
    except ValueError:
        pass


def test_get_transaction_amount_rub(fxtr_mock_transactions):
    """Тест подсчета суммы"""

    transaction_id = 1
    result = get_transaction_amount(fxtr_mock_transactions, transaction_id)
    assert result == "100.00"


def test_get_transaction_amount_usd(fxtr_mock_transactions):
    """Тест конвертации в доллары"""

    transaction_id = 2
    with patch("utils.transactions.convert_currency") as mock_convert:
        mock_convert.return_value = 75.0
        result = get_transaction_amount(fxtr_mock_transactions, transaction_id)
        assert result == 75.0


def test_get_transaction_amount_eur(fxtr_mock_transactions):
    """Тест конвертации в евро"""

    transaction_id = 3
    with patch("utils.transactions.convert_currency") as mock_convert:
        mock_convert.return_value = 90.0
        result = get_transaction_amount(fxtr_mock_transactions, transaction_id)
        assert result == 90.0


def test_get_transaction_amount_not_found(fxtr_mock_transactions):
    """Тест на отсутствие конкретной транзакции"""

    transaction_id = 4
    result = get_transaction_amount(fxtr_mock_transactions, transaction_id)
    assert result == "Транзакция не найдена"


def test_get_transactions_from_csv():
    """Тест чтения из CSV файла"""
    file_path = r"C:\Users\BSan\Desktop\SP\SP9\tests\test_data\transactions.csv"
    transactions = get_transaction_from_csv(file_path)
    assert len(transactions) == 12  # предположим, что в файле содержится 12 строк данных


def test_get_transactions_from_xlsx():
    """Тест чтения из XLSX файла"""
    file_path = r"C:\Users\BSan\Desktop\SP\SP9\tests\test_data\transactions_excel.xlsx"
    transactions = get_transaction_from_xlsx(file_path)
    assert len(transactions) == 17  # предположим, что в файле содержится 17 строк данных
