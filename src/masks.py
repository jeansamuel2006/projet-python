def get_mask_card_number(card_number: int) -> str:
    number = str(card_number)
    if len(number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    first = number[:6]
    last = number[-4:]
    return f"{first[:4]} {first[4:]}** **** {last}"


def get_mask_account(account_number: int) -> str:
    number = str(account_number)
    if len(number) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")
    last = number[-4:]
    return f"**{last}"
