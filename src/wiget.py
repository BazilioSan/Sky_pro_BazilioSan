from src.masks import get_card_mask
from src.masks import get_account_mask


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


def extraction_date(exact_time: str) -> str:
    """Функция вывода только даты в европейском формате из точной даты и времени в американском формате"""

    # Выделяем срезами нужные индексы в исходных данных, так как их формат всегда одинаковый
    date: str = exact_time[8:10]
    month: str = exact_time[5:7]
    year: str = exact_time[:4]

    return "".join(date) + "." + "".join(month) + "." + "".join(year)


# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ 1


def get_matching_strings(input_list: list) -> list:
    """Функция, возвращающая список строк с совпадающими первой и последней буквами."""
    result_list = []
    for string in input_list:
        if string[0] == string[-1]:
            result_list.append(string)
    return result_list


# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ 2


def max_multiply(digit_list: list) -> int :
    """Функция, возвращающая максимальное произведение двух элементов списка."""
    result = 0
    if len(digit_list) >= 2:
        for i in range(len(digit_list)):
            for j in range(i + 1, len(digit_list)):
                multiply_result = digit_list[i] * digit_list[j]
                if multiply_result > result:
                    result = multiply_result
        return result
    else:
        return 0
