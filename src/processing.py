from typing import Iterable
from typing import Any


def filter_by_state(list_of_data: Any, state: str = "EXECUTED") -> Iterable[dict]:
    """Функция, возвращающая список словарей с указанным состоянием."""

    result = []

    # for dictionary in list_of_data:
    #     if dictionary["state"] == state:
    #         result.append(dictionary)

    for dictionary in list_of_data:
        if dictionary.get("state") == state:
            result.append(dictionary)

    return result


def sort_by_date(list_of_dicts: Any, order: bool = True) -> Iterable[dict]:
    """Функция, возвращающая список словарей, отсортированных по дате."""

    result = sorted(list_of_dicts, key=lambda x: x["date"], reverse=order)

    return result
