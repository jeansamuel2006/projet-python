import json
from typing import Any


def load_transactions(path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список транзакций (или пустой список)."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    if isinstance(data, list):
        return data
    return []
