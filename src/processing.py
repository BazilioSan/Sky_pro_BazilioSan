from typing import Iterable
from typing import Any
from datetime import datetime


def filter_by_state(list_of_data: Any, state: str = "EXECUTED") -> Iterable[dict]:
    """Функция, возвращающая список словарей с указанным состоянием."""

    result = []

    for dictionary in list_of_data:
        if dictionary.get("state") == state:
            result.append(dictionary)
    return result

    # return [dictionary for dictionary in list_of_data if dictionary.get("state") == state]


def sort_by_date(list_of_dicts: Any, order: bool = True) -> Iterable[dict]:
    """Функция, возвращающая список словарей, отсортированных по дате."""

    # result = sorted(list_of_dicts, key=lambda x: x["date"], reverse=order)
    # result = sorted(list_of_dicts, key=lambda x: datetime.fromisoformat(x["date"]), reverse=order)
    result = sorted(list_of_dicts, key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%SZ'), reverse=order)

    return result
