import json


def get_transactions_dictionary(file_json: str) -> list:
    try:
        with open(file_json, 'r', encoding="UTF=8") as f:
            try:
                transactions = json.load(f)
                if transactions == []:
                    return []
            except UnicodeDecodeError:
                return []
    except FileNotFoundError:
        return []
    return transactions

if __name__ == '__main__':
    file_json = "../data/operations.json"
    print(get_transactions_dictionary(file_json))