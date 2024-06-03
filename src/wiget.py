from typing import Union
from masks import get_card_mask
from masks import get_account_mask


def mask_of_data(bank_user_data: Union[str, int]) -> str:
    """Функция маскировки части пользовательских данных звездочками, в случае если данные Карта/счет + номер"""

    mask_number: list = []
    type_of_data: list = []

    # Проходим по входным данным и отделяем тип от номера
    for data in bank_user_data:
        if data.isdigit():
            mask_number.append(data)
        elif data.isalpha():
            type_of_data.append(data)

    # Определяем функцию маскировки исходя из длины номера карты/счета
    if len(mask_number) == 16:
        return "".join(type_of_data) + " " + get_card_mask("".join(mask_number))

    elif len(mask_number) == 20:
        return "".join(type_of_data) + " " + get_account_mask("".join(mask_number))


def extraction_date(exact_time: Union[str, int]) -> str:
    """Функция вывода только даты в европейском формате из точной даты и времени в американском формате"""

    format_date = str(exact_time)

    date: list = [format_date]

    print(date)


z = mask_of_data("MasterCard 7158300734726758")
c = mask_of_data("Счет 73654108430135874305")
q = extraction_date("2018-07-11T02:26:18.671407")

print(z)
print(c)
print(q)
