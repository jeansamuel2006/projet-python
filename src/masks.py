import logging
import os

# Chemin absolu vers le dossier logs à la racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)  # crée logs/ s'il n'existe pas

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    os.path.join(LOGS_DIR, "masks.log"), mode="w", encoding="utf-8"
)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    number = str(card_number)
    if len(number) != 16:
        logger.error("Неверный номер карты: ожидается 16 цифр")
        raise ValueError("Номер карты должен содержать 16 цифр")
    first = number[:6]
    last = number[-4:]
    logger.info("Номер карты успешно замаскирован")
    return f"{first[:4]} {first[4:]}** **** {last}"


def get_mask_account(account_number: int) -> str:
    number = str(account_number)
    if len(number) != 20:
        logger.error("Неверный номер счёта: ожидается 20 цифр")
        raise ValueError("Номер счёта должен содержать 20 цифр")
    last = number[-4:]
    logger.info("Номер счёта успешно замаскирован")
    return f"**{last}"
