from typing import Any

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрации операций по ключу"""
    new_data = []
    for key in data:
        if key.get("state") == state:
            new_data.append(key)
    return new_data


print(filter_by_state(data, "CANCELED"))


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Фунуия сортировки операций по дате"""
    sorted_data = sorted(data, key=lambda data: data["date"], reverse=reverse)
    return sorted_data


print(sort_by_date(data))
