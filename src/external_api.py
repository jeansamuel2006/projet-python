import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях (float)."""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": API_KEY or ""}  # ← garantit une str
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return float(data["result"])
