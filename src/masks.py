def get_mask_card_number(card_number: int) -> str:
    number = str(card_number)
    if len(number) != 16:  # верификация цифр
        return "номер не правильно"
    first = number[:6]
    last = number[-4:]
    return f"{first[:4]} {first[4:]}** **** {last}"


def get_mask_account(account_number: int) -> str:
    number = str(account_number)
    if len(number) != 20:  # верификация цифр
        return "номер не правильно"
    last = number[-4:]
    return f"**{last}"
