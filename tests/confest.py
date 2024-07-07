from typing import Any

import pytest

from src.processing import data


@pytest.fixture
def test_info_state() -> str:
    return "EXECUTED"


@pytest.fixture
def test_info_state_1() -> list[dict[Any, Any]]:
    return data
