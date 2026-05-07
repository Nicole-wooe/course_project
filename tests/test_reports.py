import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from reports import spending_by_category


def test_spending_by_category():
    df = pd.DataFrame({
        "Категория": [
            "Супермаркеты",
            "Супермаркеты",
            "Такси",
        ],
        "Сумма операции": [
            -100,
            -200,
            -50,
        ],
    })

    result = spending_by_category(df, "Супермаркеты")

    assert result["category"] == "Супермаркеты"
    assert result["total_spent"] == 300.0
    assert result["operations_count"] == 2
