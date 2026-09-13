import json
import logging
import os
from typing import Any

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(path: str) -> list[dict[str, Any]]:
    """Read a JSON file and return a list of transactions (or empty list)."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Failed to read file: %s", path)
        return []
    if isinstance(data, list):
        logger.info("Loaded transactions: %s", len(data))
        return data
    logger.warning("File does not contain a list")
    return []


def load_transactions_csv(path: str) -> list[dict[str, Any]]:
    """Read transactions from a CSV file and return a list of dicts."""
    df = pd.read_csv(path, delimiter=";")
    return df.to_dict(orient="records")


def load_transactions_xlsx(path: str) -> list[dict[str, Any]]:
    """Read transactions from an XLSX file and return a list of dicts."""
    df = pd.read_excel(path)
    return df.to_dict(orient="records")
