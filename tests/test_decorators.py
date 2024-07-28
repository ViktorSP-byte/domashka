import pytest
import os

from src.decorators import log


def test_log_to_print_success(capsys):
    @log()
    def divider(x, y):
         return x / y
    result = divider(4, 2)
    assert result == 2.0

    captured = capsys.readouterr()
    assert 'divider ok' in captured.out


def test_log_to_print_error_zero_division(capsys):
    @log()
    def divider(x, y):
         return x / y

    with pytest.raises(ZeroDivisionError):
        divider(4, 0)

    captured = capsys.readouterr()
    assert 'divider error: division by zero. Inputs: (4, 0), {}' in captured.out


def test_log_to_log_file_success():
    CURRENT_PATH = os.path.dirname(__file__)
    LOG_FILE = os.path.join(CURRENT_PATH, 'test_log.txt')

    @log(LOG_FILE)
    def divider(x, y):
         return x / y

    result = divider(4, 2)
    assert result == 2.0

    with open(LOG_FILE) as file:
        content = file.read()
    assert 'divider ok' in content
    os.remove(LOG_FILE)


def test_log_to_log_file_error_zero_division():
    CURRENT_PATH = os.path.dirname(__file__)
    LOG_FILE = os.path.join(CURRENT_PATH, 'test_log_error.txt')
    @log(LOG_FILE)
    def divider(x, y):
         return x / y
    with pytest.raises(ZeroDivisionError):
        divider(4, 0)

    with open(LOG_FILE) as file:
        content = file.read()
    assert 'divider error: division by zero. Inputs: (4, 0), {}' in content
    os.remove(LOG_FILE)
