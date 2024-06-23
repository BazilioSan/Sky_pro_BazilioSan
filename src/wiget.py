from src.masks import get_account_mask, get_card_mask


def mask_of_data(bank_user_data: str) -> str:
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

    return "Ошибка при вводе данных"


def extraction_date(exact_time: str) -> str:
    """Функция вывода только даты в европейском формате из точной даты и времени в американском формате"""

    # Выделяем срезами нужные индексы в исходных данных, так как их формат всегда одинаковый
    date: str = exact_time[8:10]
    month: str = exact_time[5:7]
    year: str = exact_time[:4]

    return "".join(date) + "." + "".join(month) + "." + "".join(year)


