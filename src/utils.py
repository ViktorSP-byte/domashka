import json


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
    file_json = "../data/operations.json"
    print(get_transactions_dictionary(file_json))