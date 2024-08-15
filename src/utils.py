import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "../logs/utils.log", encoding="utf-8"
)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_transactions_dictionary(file_json: str) -> list:
    """Функция, принимающая путь до JSON файла
     и возвращает спсисок словарей с данными о финансовых транзакциях """
    try:
        with open(file_json, 'r', encoding="UTF=8") as f:
            try:
                transactions = json.load(f)
                return transactions
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return transactions


if __name__ == '__main__':
    file_json = ".../data/operations.json"
    print(get_transactions_dictionary(file_json))
