from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    result = []
    for item in data:
        if item["state"] == state:
            result.append(item)
    return result


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
