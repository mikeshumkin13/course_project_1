import pandas as pd


def read_operations(file_path: str) -> pd.DataFrame:
    """Читает данные о транзакциях из Excel файла и возвращает DataFrame."""
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame в случае ошибки


def filter_operations(
    df: pd.DataFrame, category: str = None, start_date: str = None, end_date: str = None
) -> pd.DataFrame:
    """Фильтрует операции по категории и датам."""
    if category:
        df = df[df["Категория"] == category]
    if start_date:
        df = df[df["Дата операции"] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df["Дата операции"] <= pd.to_datetime(end_date)]
    return df


def get_last_4_digits(card_number):
    """Возвращает последние 4 цифры номера карты."""
    return str(card_number)[-4:]


def calculate_total_spent(transactions):
    """Считает общую сумму расходов по транзакциям."""
    return transactions["Сумма операции"].sum()


def calculate_cashback(total_spent):
    """Вычисляет кэшбэк из расчета 1 рубль на каждые 100 рублей."""
    return total_spent // 100  # 1 рубль на каждые 100 рублей


def get_top_5_transactions(transactions):
    """Возвращает топ-5 транзакций по сумме."""
    return transactions.nlargest(5, "Сумма операции")[
        ["Дата операции", "Сумма операции", "Категория", "Описание"]
    ]
