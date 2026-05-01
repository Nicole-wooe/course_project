import pandas as pd


def spending_by_category(transactions: pd.DataFrame, category: str):
    filtered = transactions[
        (transactions["Категория"] == category)
        & (transactions["Сумма операции"] < 0)
    ]

    total = float(abs(filtered["Сумма операции"].sum()))

    return {
        "category": category,
        "total_spent": round(total, 2),
        "operations_count": len(filtered)
    }
