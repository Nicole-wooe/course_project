import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from services import get_top_transactions
import pandas as pd

def test_top_transactions():
    df = pd.DataFrame({
        "Сумма операции": [-100, -200, -50],
        "Дата операции": pd.to_datetime(["2021-01-01", "2021-01-02", "2021-01-03"]),
        "Категория": ["A", "B", "C"],
        "Описание": ["x", "y", "z"]
    })

    result = get_top_transactions(df)

    assert len(result) == 3

import pandas as pd
from services import get_cards


def test_get_cards():
    data = {
        "Номер карты": ["1234", "1234", "5678"],
        "Сумма операции": [-100, 200, -50],
        "Дата операции": pd.to_datetime([
            "2021-12-30",
            "2021-12-31",
            "2021-12-29"
        ]),
        "Категория": ["Еда", None, "Транспорт"],
        "Описание": ["Кафе", "Зарплата", "Такси"]
    }

    df = pd.DataFrame(data)

    result = get_cards(df)

    assert len(result) == 2
    assert result[0]["card_number"].startswith("****")
    assert "last_transactions" in result[0]
    