import pandas as pd

from src.views import get_greeting, home_page


def test_get_greeting_morning():
    assert get_greeting("2021-12-31 08:00:00") == "Доброе утро"


def test_get_greeting_day():
    assert get_greeting("2021-12-31 14:00:00") == "Добрый день"


def test_get_greeting_evening():
    assert get_greeting("2021-12-31 19:00:00") == "Добрый вечер"


def test_get_greeting_night():
    assert get_greeting("2021-12-31 02:00:00") == "Доброй ночи"


def test_home_page():
    df = pd.DataFrame({
        "Номер карты": ["1234", "1234", "5678"],
        "Сумма операции": [-100, 200, -50],
        "Дата операции": pd.to_datetime([
            "2021-12-30",
            "2021-12-31",
            "2021-12-29",
        ]),
        "Категория": ["Еда", "Зарплата", "Транспорт"],
        "Описание": ["Кафе", "Доход", "Такси"],
    })

    result = home_page("2021-12-31 14:00:00", df)

    assert '"greeting": "Добрый день"' in result
    assert '"cards"' in result
    assert '"top_transactions"' in result
    assert '"currency_rates": []' in result
    assert '"stock_prices": []' in result
