from src.utils import get_greeting
from datetime import datetime


def test_get_greeting():
    morning = datetime(2023, 1, 1, 8, 0, 0)
    assert get_greeting(morning) == "Доброе утро"

    day = datetime(2023, 1, 1, 13, 0, 0)
    assert get_greeting(day) == "Добрый день"

    evening = datetime(2023, 1, 1, 19, 0, 0)
    assert get_greeting(evening) == "Добрый вечер"

    night = datetime(2023, 1, 1, 2, 0, 0)
    assert get_greeting(night) == "Доброй ночи"
