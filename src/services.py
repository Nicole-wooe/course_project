import pandas as pd


def get_top_transactions(transactions):
    top_df = (
        transactions
        .sort_values("Сумма операции", ascending=True)
        .head(5)
    )

    result = []

    for _, row in top_df.iterrows():
        result.append({
            "date": row["Дата операции"].strftime("%d.%m.%Y"),
            "amount": round(abs(row["Сумма операции"]), 2),
            "category": (
                row["Категория"]
                if pd.notna(row["Категория"])
                else "Не указано"
            ),
            "description": row["Описание"],
        })

    return result


def get_cards(transactions):
    cards = (
        transactions
        .groupby("Номер карты")["Сумма операции"]
        .sum()
        .reset_index()
    )

    cards_list = []

    for _, row in cards.iterrows():
        card_number = str(row["Номер карты"])
        masked_card_number = "****" + card_number[-4:]

        card_transactions = (
            transactions[transactions["Номер карты"] == row["Номер карты"]]
            .sort_values("Дата операции", ascending=False)
            .head(3)
        )

        last_transactions = []

        for _, tr in card_transactions.iterrows():
            last_transactions.append({
                "date": tr["Дата операции"].strftime("%d.%m.%Y"),
                "amount": round(abs(tr["Сумма операции"]), 2),
                "type": (
                    "expense"
                    if tr["Сумма операции"] < 0
                    else "income"
                ),
                "category": (
                    tr["Категория"]
                    if pd.notna(tr["Категория"])
                    else "Не указано"
                ),
                "description": tr["Описание"],
            })

        cards_list.append({
            "card_number": masked_card_number,
            "total_amount": round(row["Сумма операции"], 2),
            "last_transactions": last_transactions,
        })

    return cards_list
