import os

import pandas as pd
import requests
from dotenv import load_dotenv

from services import (calculate_cashback, calculate_total_spent,
                      get_last_4_digits, get_top_5_transactions,
                      read_operations)
from utils import get_greeting

load_dotenv()

# Получение API ключей
exchange_rate_api_key = os.getenv('EXCHANGE_RATE_API_KEY')
alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')


def get_exchange_rate(api_key, currency="USD"):
    """Получает курс валюты (USD -> RUB) из внешнего API."""
    url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["rates"]["RUB"]
    return None


def get_sp500_stock_price(api_key):
    """Получает цену акций S&P 500 (SPY) из внешнего API."""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SPY&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["Global Quote"]["05. price"]
    return None


def generate_main_page_response(input_time, file_path, exchange_rate_api_key, alpha_vantage_api_key):
    # Приветствие
    current_time = pd.to_datetime(input_time)
    greeting = get_greeting(current_time)

    # Данные о транзакциях
    transactions = read_operations(file_path)
    card_data = []

    for card_number in transactions['Номер карты'].unique():
        card_transactions = transactions[transactions['Номер карты'] == card_number]
        total_spent = calculate_total_spent(card_transactions)
        cashback = calculate_cashback(total_spent)
        top_5_transactions = get_top_5_transactions(card_transactions)

        card_data.append({
            "last_4_digits": get_last_4_digits(card_number),
            "total_spent": total_spent,
            "cashback": cashback,
            "top_5_transactions": top_5_transactions.to_dict(orient="records")
        })

    # Внешние данные
    exchange_rate = get_exchange_rate(exchange_rate_api_key)
    sp500_price = get_sp500_stock_price(alpha_vantage_api_key)

    # Финальный JSON
    response = {
        "greeting": greeting,
        "cards": card_data,
        "exchange_rate": exchange_rate,
        "sp500_price": sp500_price
    }

    return response