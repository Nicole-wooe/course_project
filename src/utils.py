from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "operations.xlsx"


def load_data():
    df = pd.read_excel(file_path, engine="openpyxl")

    # дата → нормальный формат
    df["Дата операции"] = pd.to_datetime(
        df["Дата операции"],
        format="%d.%m.%Y %H:%M:%S"
    )

    # сумма → число
    df["Сумма операции"] = (
        df["Сумма операции"]
        .astype(str)
        .str.replace(",", ".")
        .astype(float)
    )

    return df
