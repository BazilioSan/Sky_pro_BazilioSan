from typing import Union
from masks import get_card_mask
from masks import get_account_mask

def mask_of_data (bank_user_data: Union[str, int]) -> str:
    """Функция маскировки части пользовательских данных звездочками, в случае если данные Карта/счет + номер"""

