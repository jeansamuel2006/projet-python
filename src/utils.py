import json
import logging
import os
from typing import Any

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
    """Читает JSON-файл и возвращает список транзакций (или пустой список)."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Не удалось прочитать файл: %s", path)
        return []
    if isinstance(data, list):
        logger.info("Загружено транзакций: %s", len(data))
        return data
    logger.warning("Файл не содержит список")
    return []
