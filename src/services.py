import pandas as pd

def read_operations(file_path: str) -> pd.DataFrame:
    """Читает данные о транзакциях из Excel файла и возвращает DataFrame."""
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame в случае ошибки

def filter_operations(df: pd.DataFrame, category: str = None, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    """Фильтрует операции по категории и датам."""
    if category:
        df = df[df['Категория'] == category]
    if start_date:
        df = df[df['Дата операции'] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df['Дата операции'] <= pd.to_datetime(end_date)]
    return df

