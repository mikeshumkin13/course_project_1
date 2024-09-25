from datetime import datetime

def get_greeting(current_time=None):
    """Возвращает приветствие в зависимости от времени суток."""
    if current_time is None:
        current_time = datetime.now()

    if 5 <= current_time.hour < 12:
        return "Доброе утро"
    elif 12 <= current_time.hour < 18:
        return "Добрый день"
    elif 18 <= current_time.hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"
