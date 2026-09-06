from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Возвращает итератор транзакций с указанной валютой."""
    return (t for t in transactions if t["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """Генератор, поочередно возвращающий описание каждой транзакции."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX от start до stop."""
    for number in range(start, stop + 1):
        card = str(number).zfill(16)
        yield f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}"
