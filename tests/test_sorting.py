import pytest
from src.sorting import sorting_transactions_by_description
from src.sorting import counting_categories

data = [
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
]


@pytest.mark.parametrize(
    "data, description, expected",
    [
        (
                data,
                "карт",
                [
                    {"id": 3598919.0, "description": "Перевод с карты на карту"},
                    {"id": 3598919.0, "description": "Перевод с карты на карту"},
                    {"id": 3598919.0, "description": "Перевод с карты на карту"},
                    {"id": 3598919.0, "description": "Перевод с карты на карту"},
                ],
        ),
        (data, "some_word", []),
        ([], "карт", []),
        (
                data,
                "организац",
                [
                    {"id": 650703.0, "description": "Перевод организации"},
                    {"id": 650703.0, "description": "Перевод организации"},
                    {"id": 650703.0, "description": "Перевод организации"},
                    {"id": 650703.0, "description": "Перевод организации"},
                ],
        ),
    ],
)
def test_sorting_transactions_by_description(data, description, expected):
    assert sorting_transactions_by_description(data, description) == expected


@pytest.mark.parametrize(
    "data, categories, expected",
    [
        (data, ["перевод с карты", "перевод Организац"], {"Перевод организации": 4, "Перевод с карты на карту": 4}),
        (data, ["перевод с карты"], {"Перевод с карты на карту": 4}),
        (data, [], {}),
        ([], ["перевод с карты", "перевод Организац"], {}),
    ],
)
def test_counting_categories(data, categories, expected):
    assert counting_categories(data, categories) == expected
