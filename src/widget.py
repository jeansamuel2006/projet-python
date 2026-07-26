from masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])
    if data.startswith("Счет"):
        masked = get_mask_account(int(number))
    else:
        masked = get_mask_card_number(int(number))
    return f"{name} {masked}"
def get_date(date_string: str) -> str:
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"