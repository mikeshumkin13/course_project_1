from dotenv import load_dotenv
import os
from reports import generate_report

# Загрузка переменных окружения из .env
load_dotenv()

# Получаем API ключи из .env
exchange_rate_api_key = os.getenv("EXCHANGE_RATE_API_KEY")
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")


base_dir = os.path.dirname(os.path.abspath(__file__))  #
file_path = os.path.join(base_dir, "../data/operations.xlsx")

if __name__ == "__main__":
    # Генерация отчета с использованием абсолютного пути
    report = generate_report(file_path)
    print(report)
