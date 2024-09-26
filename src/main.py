from dotenv import load_dotenv
import os
from views import generate_main_page_response

# Загрузка переменных окружения из .env
load_dotenv()

# Получаем API ключи из .env
exchange_rate_api_key = os.getenv('EXCHANGE_RATE_API_KEY')
alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

base_dir = os.path.dirname(os.path.abspath(__file__))  #
file_path = os.path.join(base_dir, '../data/operations.xlsx')

if __name__ == "__main__":
    # Пример времени, передаваемого в качестве входного параметра
    input_time = "2024-09-26 14:30:00"

    # Генерация главной страницы
    main_page_response = generate_main_page_response(input_time, file_path, exchange_rate_api_key,
                                                     alpha_vantage_api_key)
    print(main_page_response)