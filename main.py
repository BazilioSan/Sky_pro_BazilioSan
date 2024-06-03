from src.masks import get_card_mask
from src.masks import get_account_mask
from src.wiget import mask_of_data
from src.wiget import extraction_date

# ДЛЯ ТЕСТОВ
x = get_card_mask(7000792289606361)
y = get_account_mask(73654108430135874305)
z = mask_of_data("MasterCard 7158300734726758")
c = mask_of_data("Счет 73654108430135874305")
q = extraction_date("2018-07-11T02:26:18.671407")

print(x)
print(y)
print(z)
print(c)
print(q)
