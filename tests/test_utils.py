from utils import load_data


def test_load_data():
    df = load_data()

    assert not df.empty
    assert "Сумма операции" in df.columns
