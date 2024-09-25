import pytest
import pandas as pd
from src.services import read_operations, filter_operations

def test_read_operations():
    df = read_operations('data/operations.xlsx')
    assert isinstance(df, pd.DataFrame)  # Проверяем, что возвращается DataFrame
    assert not df.empty  # Проверяем, что файл прочитан корректно

def test_filter_operations():
    df = read_operations('data/operations.xlsx')
    filtered_df = filter_operations(df, category='Супермаркеты')
    assert all(filtered_df['Категория'] == 'Супермаркеты')
