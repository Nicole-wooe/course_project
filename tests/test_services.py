import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from services import get_cards, get_top_transactions


def test_get_top_transactions():
    df = pd.DataFrame({
        "Сумма операции": [-100, -300, -50, -200, -500, -10],
        "Дата операции": pd.to_datetime([
            "2021-01-01",
            "2021-01-02",
            "2021-01-03",
            "2021-01-04",
            "2021-01-05",
            "2021-01-06",
        ]),
        "Категория": ["A", "B", None, "D", "E", "F"],
        "Описание": ["one", "two", "three", "four", "five", "six"],
    })

    result = get_top_transactions(df)

    assert len(result) == 5
    assert result[0]["amount"] == 500
    assert result[0]["date"] == "05.01.2021"
    assert result[2]["category"] == "D"


def test_get_cards():
    df = pd.DataFrame({
        "Номер карты": ["1234", "1234", "5678"],
        "Сумма операции": [-100, 200, -50],
        "Дата операции": pd.to_datetime([
            "2021-12-30",
            "2021-12-31",
            "2021-12-29",
        ]),
        "Категория": ["Еда", None, "Транспорт"],
        "Описание": ["Кафе", "Зарплата", "Такси"],
    })

    result = get_cards(df)

    assert len(result) == 2
    assert result[0]["card_number"].startswith("****")
    assert "last_transactions" in result[0]
    assert result[0]["last_transactions"][0]["type"] in ["expense", "income"]
