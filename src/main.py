import os
from dotenv import load_dotenv

from reports import generate_report
from views import generate_main_page_response
from services import filter_operations, search_transactions_service, read_operations

# Загрузка переменных окружения из .env
load_dotenv()

# Получаем API ключи из .env
exchange_rate_api_key = os.getenv('EXCHANGE_RATE_API_KEY')
alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

base_dir = os.path.dirname(os.path.abspath(__file__))  # Получаем директорию текущего файла
file_path = os.path.join(base_dir, '../data/operations.xlsx')  # Путь к файлу операций


def display_menu():
    print("\nВыберите действие:")
    print("1. Сгенерировать отчет")
    print("2. Поиск транзакций")
    print("3. Выход")


def generate_report_action():
    # Логика для генерации отчета
    print("\nГенерация отчета...")
    report = generate_report(file_path)  # Вызов функции генерации отчета
    print("Отчет сгенерирован и сохранен в 'report.json'.")


def search_transactions_action():
    # Логика для поиска транзакций
    print("\nПоиск транзакций...")
    search_term = input("Введите строку для поиска: ")
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
    while True:
        display_menu()
        choice = input("Введите номер действия: ")

        if choice == '1':
            generate_report_action()
        elif choice == '2':
            search_transactions_action()
        elif choice == '3':
            print("Выход...")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
