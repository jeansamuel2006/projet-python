 # Проект по маскировке и обработке банковских данных

Учебный проект на Python для работы с данными о банковских картах, счетах
и операциях: маскировка номеров, фильтрация и сортировка транзакций.

## Возможности

Проект содержит следующие модули в директории `src`:

- **`masks`** — маскировка номеров карт и счетов.
- **`widget`** — обработка строк с типом и номером, форматирование дат.
- **`processing`** — фильтрация и сортировка списков операций.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/jeansamuel2006/projet-python.git
cd projet-python
```

2. Установите зависимости с помощью Poetry:

```bash
poetry install --with lint
```

## Использование

### Маскировка номера карты и счёта (`masks`)

```python
from masks import get_mask_card_number, get_mask_account

get_mask_card_number(7000792289606361)
# 7000 79** **** 6361

get_mask_account(73654108430135874305)
# **4305
```

### Обработка карт, счетов и дат (`widget`)

```python
from widget import mask_account_card, get_date

mask_account_card("Visa Platinum 7000792289606361")
# Visa Platinum 7000 79** **** 6361

mask_account_card("Счет 73654108430135874305")
# Счет **4305

get_date("2024-03-11T02:26:18.671407")
# 11.03.2024
```

### Фильтрация и сортировка операций (`processing`)

```python
from processing import filter_by_state, sort_by_date

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

# Фильтрация по статусу (по умолчанию "EXECUTED")
filter_by_state(data)
# [{'id': 41428829, ...}, {'id': 939719570, ...}]

filter_by_state(data, "CANCELED")
# [{'id': 594226727, ...}]

# Сортировка по дате (по умолчанию по убыванию)
sort_by_date(data)
# сначала самые последние операции
```

## Проверка качества кода

```bash
poetry run black src
poetry run isort src
poetry run flake8 src
poetry run mypy src
```
### Генераторы (`generators`)

Модуль `generators` содержит функции для работы с большими объёмами данных
транзакций через генераторы.

```python
from generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фильтрация транзакций по валюте (возвращает итератор)
usd = filter_by_currency(transactions, "USD")
next(usd)

# Описание каждой транзакции по очереди
descriptions = transaction_descriptions(transactions)
next(descriptions)

# Генерация номеров карт в заданном диапазоне
for card in card_number_generator(1, 5):
    print(card)
# 0000 0000 0000 0001 ... 0000 0000 0000 0005
```