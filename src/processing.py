def filter_by_state(list_of_data, state="CANCELED"):
    """Функция, возвращающая список словарей с указанным состоянием."""

    result = []
    for dict in list_of_data:
        if dict["state"] == state:
            result.append(dict)

    return result

def sort_by_date(list_of_dicts, order = True):
    """Функция, возвращающая список словарей, отсортированных по дате."""

    result = sorted(list_of_dicts, key=lambda x: x["date"], reverse=order)

    return result

