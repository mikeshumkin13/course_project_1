import os
import pytest
from unittest.mock import patch
import pandas as pd

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from main import main, generate_report_action, search_transactions_action


def test_display_menu_exit():
    # Тестируем, что при выборе '3' приложение завершает работу
    with patch("builtins.input", return_value="3"), patch("builtins.print") as mocked_print:
        main()
        mocked_print.assert_any_call("Выход...")


def test_display_menu_invalid_choice():
    # Тестируем, что при некорректном вводе выводится сообщение об ошибке
    with patch("builtins.input", side_effect=["4", "3"]), patch("builtins.print") as mocked_print:
        main()
        mocked_print.assert_any_call("Некорректный выбор, попробуйте снова.")
        mocked_print.assert_any_call("Выход...")


def test_generate_report_action():
    with patch("main.generate_report") as mocked_generate_report:
        generate_report_action()
        # Теперь проверяем, что вызывается с правильным путем
        base_dir = os.path.dirname(__file__)  # Получаем директорию теста
        expected_path = os.path.abspath(os.path.join(base_dir, "../data/operations.xlsx"))
        mocked_generate_report.assert_called_once_with(expected_path)


def test_search_transactions_action():
    # Тестируем, что при вызове search_transactions_action вызывается search_transactions_service
    from services import search_transactions_service, read_operations

    with patch("builtins.input", return_value="Аптеки"), patch(
        "main.read_operations"
    ) as mocked_read_operations, patch(
        "main.search_transactions_service"
    ) as mocked_search_transactions_service, patch(
        "builtins.print"
    ) as mocked_print:
        # Мокируем возвращаемые данные
        mocked_read_operations.return_value = pd.DataFrame(
            {
                "Описание": ["Покупка лекарств", "Оплата услуг"],
                "Категория": ["Аптеки", "Услуги"],
                "Дата операции": ["2023-01-01", "2023-01-02"],
                "Сумма операции": [-500, -1500],
            }
        )
        mocked_search_transactions_service.return_value = [
            {
                "Описание": "Покупка лекарств",
                "Категория": "Аптеки",
                "Дата операции": "2023-01-01",
                "Сумма операции": -500,
            }
        ]

        search_transactions_action()

        # Проверяем, что была вызвана функция поиска с правильными параметрами
        mocked_search_transactions_service.assert_called_once_with(mocked_read_operations.return_value, "Аптеки")

        # Проверяем, что результаты поиска были напечатаны
        mocked_print.assert_any_call("Найдено 1 транзакций:")
        mocked_print.assert_any_call(
            {
                "Описание": "Покупка лекарств",
                "Категория": "Аптеки",
                "Дата операции": "2023-01-01",
                "Сумма операции": -500,
            }
        )
