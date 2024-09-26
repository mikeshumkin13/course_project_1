from dotenv import load_dotenv
import os

load_dotenv()

# Получение API ключей
exchange_rate_api_key = os.getenv("EXCHANGE_RATE_API_KEY")
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
