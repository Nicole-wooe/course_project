from views import get_greeting


def test_get_greeting_morning():
    assert get_greeting("2021-12-31 08:00:00") == "Доброе утро"


def test_get_greeting_day():
    assert get_greeting("2021-12-31 14:00:00") == "Добрый день"


def test_get_greeting_evening():
    assert get_greeting("2021-12-31 19:00:00") == "Добрый вечер"


def test_get_greeting_night():
    assert get_greeting("2021-12-31 02:00:00") == "Доброй ночи"
