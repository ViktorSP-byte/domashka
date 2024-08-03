from src.masks import get_mask_account, get_mask_card_number
from processing import data

def mask_account_card(account_info: str) -> str:
    """Функция, возвращающая маску карты или счета"""
    if account_info[:4] == "Счет":
        account_number = get_mask_account(account_info[5:])
        mask_account = f"{account_info[:4]} {account_number}"
        return mask_account
    else:
        mask_card_number = get_mask_card_number(account_info[-16:])
        mask_card = f"{account_info[:-16]} {mask_card_number}"
        return mask_card


def filter_alpha_data(data_client: str):
    """функция возвращает только название карты или счета"""
    alpha_data = ""

    for el in list(data_client):
        if el.isalpha() or el == " ":
            alpha_data += el

    return alpha_data


def get_data(data: list) -> list:
    """Функция, меняющая формат даты"""
    result = data[8: 10] + "." + data[5:7] + "." + data[0:4]
    return result


