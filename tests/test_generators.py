import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод со счета на счет"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод с карты на карту"},
    ]


def test_filter_by_currency(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result[0] == "Перевод организации"
    assert len(result) == 3


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected
