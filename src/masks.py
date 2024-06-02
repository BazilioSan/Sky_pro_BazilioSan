from typing import Union


def get_card_mask(card_number: Union[str, int]) -> str:
    """Функция маскировки части номера карты звездочками"""

    mask_number: list = []

    # Преобразует вводные данные в строку (если введено просто число), а из нее делает список
    format_number = str(card_number)
    card_parts = list(format_number)

    # Срезами разделяет номер на части
    first_part = card_parts[0:4]
    second_part = card_parts[4:6]
    second_part.append("**")
    third_part = "****"
    forth_part = card_parts[-4:]

    # Конкатенируем результат и в выводе добавляет пробелы между частями
    mask_number.append("".join(first_part))
    mask_number.append("".join(second_part))
    mask_number.append("".join(third_part))
    mask_number.append("".join(forth_part))

    return " ".join(mask_number)


def get_account_mask(account_number: Union[str, int]) -> str:
    """Функция маскировки части счета звездочками"""

    mask_number: list = ["**"]

    # Преобразовывает ввод в строку (если введено просто число), а потом в список
    format_number = str(account_number)
    account_parts = list(format_number)

    # Делает срез последних 4 чисел счета и добавляет их в результат
    first_part = account_parts[-4:]
    mask_number.append("".join(first_part))

    return "".join(mask_number)
