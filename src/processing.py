def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    result = []
    for item in data:
        if item["state"] == state:
            result.append(item)
    return result


def sort_by_date(data: list, reverse: bool = True) -> list:
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
