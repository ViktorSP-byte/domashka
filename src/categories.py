import logging

from typing import Any
from utils import get_transactions_dictionary
from generators import transaction_descriptions
from collections import Counter

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    "../logs/descriptions.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def list_categories(transactions):

    return (
        transaction["description"]
        for transaction in transactions
        if "description" in transaction
    )


def categories_by_descriptions(transactions: list[dict[str, Any]], categories: list[str]) -> dict:
    descriptions = [description for description in transaction_descriptions(transactions) if description in categories]
    return dict(Counter(descriptions))


if __name__ == "__main__":
    path = ".../data/operations.json"
    list_trans = get_transactions_dictionary(path)
    # print(*list_categories(list_trans), sep="\n")
    categories = list_categories(list_trans)
    print(categories_by_descriptions(list_trans, categories))