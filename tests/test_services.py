import pytest
import sys
import os
import pandas as pd

# Добавляем путь к src в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from services import (
    get_last_4_digits,
    calculate_total_spent,
    calculate_cashback,
    get_top_5_transactions,
    search_transactions_service,
)


def test_get_last_4_digits():
    assert get_last_4_digits("1234567890123456") == "3456"


def test_calculate_total_spent():
    transactions = pd.DataFrame({"Сумма операции": [100, 200, 300]})
    assert calculate_total_spent(transactions) == 600


def test_calculate_cashback():
    assert calculate_cashback(600) == 6


def test_get_top_5_transactions():
    transactions = pd.DataFrame(
        {
            "Дата операции": ["2023-01-01", "2023-01-02"],
            "Сумма операции": [200, 100],
            "Категория": ["Категория1", "Категория2"],
            "Описание": ["Описание1", "Описание2"],
        }
    )
    top_5 = get_top_5_transactions(transactions)
    assert len(top_5) == 2


def test_search_transactions_service():
    transactions = pd.DataFrame(
        {
            "Описание": ["Покупка лекарств", "Покупка продуктов"],
            "Категория": ["Аптеки", "Супермаркеты"],
            "Дата операции": ["2023-01-01", "2023-01-02"],
            "Сумма операции": [-500, -1500],
        }
    )
    query = "Аптеки"
    results = search_transactions_service(transactions, query)

    assert isinstance(results, list)  # Проверяем, что результат — это список
    assert len(results) == 1  # Ожидаем, что найдена одна транзакция
    assert results[0]["Категория"] == "Аптеки"  # Проверяем значение категории
    assert results[0]["Описание"] == "Покупка лекарств"  # Проверяем значение описания
    assert results[0]["Сумма операции"] == -500  # Проверяем значение суммы операции
