from src.masks import get_card_mask
from src.masks import get_account_mask

from src.wiget import mask_of_data
from src.wiget import extraction_date

from src.processing import filter_by_state
from src.processing import sort_by_date

from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator



# ДЛЯ ТЕСТОВ
# x = get_card_mask(7000792289606361)
# y = get_account_mask(73654108430135874305)
# z = mask_of_data("MasterCard 7158300734726758")
# c = mask_of_data("Счет 73654108430135874305")
# q = extraction_date("2018-07-11T02:26:18.671407")
# w = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
# e = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
# transactions = [{
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {
#             "amount": "43318.34",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160"
#     },
#     {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {
#             "amount": "56883.54",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод с карты на карту",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229"
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {
#             "amount": "67314.70",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657"
#     }
# ]


# print(x)
# print(y)
# print(z)
# print(c)
# print(q)
# print(w)
# print(e)

# usd_transactions = filter_by_currency(transactions, "USD")
# for x in range(2):
#     print(next(usd_transactions)["id"])
#
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#   print(next(descriptions))
#
# for card_number in card_number_generator(48, 50):
#   print(card_number)
