import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "C:/Users/RobotComp.ru/PycharmProjects/course2_homeworks/logs/masks.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

def get_mask_card_number(card_2: str) -> str:
    """Функция, маскирующая номер карты"""
    return card_2.replace(card_2[6:-4], "******")


def get_mask_account(card_1: str) -> str:
    """ "Функция, маскирующая номер счета"""
    return card_1.replace(card_1[:-4], "**")
