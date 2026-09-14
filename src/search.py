import re
from typing import Any


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """Count transactions per category based on description."""
    result = {}
    for category in categories:
        count = 0
        for transaction in data:
            if transaction.get("description") == category:
                count += 1
        result[category] = count
    return result


def process_bank_search(data: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    """Return transactions whose description contains the search string."""
    pattern = re.compile(search, re.IGNORECASE)
    return [transaction for transaction in data if pattern.search(transaction.get("description", ""))]


# --- test temporaire ---
data = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Открытие вклада"},
    {"id": 3, "description": "Перевод организации"},
]

categories = ["Перевод организации", "Открытие вклада"]
result = process_bank_operations(data, categories)
print(result)  # {'Перевод организации': 2, 'Открытие вклада': 1}
