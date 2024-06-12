from src.masks import get_card_mask
from src.masks import get_account_mask
from src.wiget import mask_of_data
from src.wiget import extraction_date
from src.processing import filter_by_state
from src.processing import sort_by_date


# ДЛЯ ТЕСТОВ
x = get_card_mask(7000792289606361)
y = get_account_mask(73654108430135874305)
z = mask_of_data("MasterCard 7158300734726758")
c = mask_of_data("Счет 73654108430135874305")
q = extraction_date("2018-07-11T02:26:18.671407")
w = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
e = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])

print(x)
print(y)
print(z)
print(c)
print(q)
print(w)
print(e)
