import json
from datetime import datetime

from src.services import get_cards, get_top_transactions


def get_greeting(date_time: str) -> str:
    user_datetime = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    hour = user_datetime.hour

    if 6 <= hour <= 11:
        return "Доброе утро"
    if 12 <= hour <= 17:
        return "Добрый день"
    if 18 <= hour <= 22:
        return "Добрый вечер"
    return "Доброй ночи"


def home_page(date_time: str, transactions):
    cards = get_cards(transactions)
    top_transactions = get_top_transactions(transactions)

    result = {
        "greeting": get_greeting(date_time),
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": [],
        "stock_prices": [],
    }

    return json.dumps(result, ensure_ascii=False, indent=4)
