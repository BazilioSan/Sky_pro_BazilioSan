# Проект домашней работы 2 курса SkyPro

## Описание:

IT-отдел крупного банка делает новую фичу для личного кабинета 
, который показывает несколько последних успешных банковских операций клиента.


## Функционал:

get_card_mask - Функция маскировки части номера карты звездочками

get_account_mask - Функция маскировки части счета звездочками

mask_of_data - Функция маскировки части пользовательских данных звездочками, в случае если данные Карта/счет + номер

extraction_date - Функция вывода только даты в европейском формате из точной даты и времени в американском формате

filter_by_state - Функция, возвращающая список словарей с указанным состоянием.

sort_by_date - Функция, возвращающая список словарей, отсортированных по дате.

filter_by_currency - Функция, возвращающая генератор номеров транзакций (id) с указанной валютой

transaction_descriptions - Функция, возвращающая генератор описаний транзакций

card_number_generator - Функция-генератор номеров карт

log - Функция логгирования в файл и консоль

## Тестирование:

Тестирование производится с помощью библиотеки pytest.
Все имеющиеся модули успешно покрыты тестами на 24.06.2024 г.

Для самостоятельного тестирования используйте модули тестирования находящиеся в пакете tests.

## Установка:

1. Клонируйте репозиторий:
```
git clone github.com/BazilioSan/Sky_pro_BazilioSan.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:


Этот проект лицензирован по [лицензии MIT](LICENSE).