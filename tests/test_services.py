import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from services import get_last_4_digits, calculate_total_spent, calculate_cashback, get_top_5_transactions
import pandas as pd

def test_get_last_4_digits():
    assert get_last_4_digits("1234567890123456") == "3456"

def test_calculate_total_spent():
    transactions = pd.DataFrame({
        "Сумма операции": [100, 200, 300]
    })
    assert calculate_total_spent(transactions) == 600

def test_calculate_cashback():
    assert calculate_cashback(600) == 6

def test_get_top_5_transactions():
    transactions = pd.DataFrame({
        "Дата операции": ["2023-01-01", "2023-01-02"],
        "Сумма операции": [200, 100],
        "Категория": ["Категория1", "Категория2"],
        "Описание": ["Описание1", "Описание2"]
    })
    top_5 = get_top_5_transactions(transactions)
    assert len(top_5) == 2