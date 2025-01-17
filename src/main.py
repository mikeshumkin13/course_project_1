import os
from dotenv import load_dotenv

from reports import generate_report
from services import read_operations, search_transactions_service
from utils import get_greeting


# Загрузка переменных окружения из .env
load_dotenv()

# Получаем API ключи из .env (если они ещё нужны для других функций)
exchange_rate_api_key = os.getenv("EXCHANGE_RATE_API_KEY")
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")


def display_menu():
    """
    Отображает главное меню приложения с доступными действиями.
    Действия:
    1. Сгенерировать отчет
    2. Поиск транзакций
    3. Выход
    """

    print("\nВыберите действие:")
    print("1. Сгенерировать отчет")
    print("2. Поиск транзакций")
    print("3. Выход")


def generate_report_action():
    """
    Генерирует отчет по транзакциям.
    Читает данные из файла `operations.xlsx`, обрабатывает их и сохраняет отчет в формате JSON.
    """

    # Получаем абсолютный путь к файлу operations.xlsx
    base_dir = os.path.dirname(__file__)  # Директория текущего файла
    file_path = os.path.abspath(os.path.join(base_dir, "../data/operations.xlsx"))  # Создаем абсолютный путь к файлу
    print("Генерация отчета...")
    generate_report(file_path)  # Вызываем функцию с правильным путем
    print("Отчет сгенерирован и сохранен в 'report.json'.")


def search_transactions_action():
    """
    Выполняет поиск транзакций по заданному критерию.
    Запрашивает у пользователя строку для поиска, фильтрует транзакции и выводит результаты.
    """
    # Логика для поиска транзакций
    print("\nПоиск транзакций...")
    search_term = input("Введите строку для поиска: ")
    file_path = "/Users/a12345/PycharmProjects/course_project_1/data/operations.xlsx"
    transactions = read_operations(file_path)
    if transactions.empty:
        print("Нет данных для поиска.")
        return
    results = search_transactions_service(transactions, search_term)
    if results:
        print(f"Найдено {len(results)} транзакций:")
        for transaction in results:
            print(transaction)
    else:
        print("Транзакции не найдены.")


def main():
    """
    Основная функция приложения.
    Отображает приветствие, меню и обрабатывает пользовательский ввод для выполнения действий.
    """
    greeting = get_greeting()
    print(f"{greeting}!\nДобро пожаловать в приложение для управления транзакциями.")

    while True:
        display_menu()
        choice = input("Введите номер действия: ")

        if choice == "1":
            generate_report_action()
        elif choice == "2":
            search_transactions_action()
        elif choice == "3":
            print("Выход...")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
