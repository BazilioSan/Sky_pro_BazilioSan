from typing import Union
import logging
import os

logs_dir = os.path.join(os.path.dirname(__file__), "..", 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_card_mask(card_number: Union[str, int]) -> str:
    """Функция маскировки части номера карты звездочками"""

    logger.info(f"Функция get_card_mask запущена с входным номером: {card_number}")

    mask_number: list = []

    # Преобразует вводные данные в строку (если введено просто число), а из нее делает список
    format_number = str(card_number)
    card_parts = list(format_number)

    # Срезами разделяет номер на части
    logger.info(f"Преобразовывает номер карты")

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
    logger.info(f"функция get_card_mask успешно отработала с результатом: {mask_number}")

    return " ".join(mask_number)


def get_account_mask(account_number: Union[str, int]) -> str:
    """Функция маскировки части счета звездочками"""

    logger.info(f"Функция get_account_mask запущена с входным номером: {account_number}")

    mask_number: list = ["**"]

    # Преобразовывает ввод в строку (если введено просто число), а потом в список

    format_number = str(account_number)
    account_parts = list(format_number)

    # Делает срез последних 4 чисел счета и добавляет их в результат
    first_part = account_parts[-4:]
    mask_number.append("".join(first_part))
    logger.info(f"Функция get_account_mask успешно отработала с результатом: {mask_number}")
    return "".join(mask_number)


a = get_account_mask(73654108430135874305)
print(a)
