from reports import spending_by_category
from utils import load_data
from views import home_page


df = load_data()

result = home_page("2021-12-31 16:44:00", df)
print(result)

report = spending_by_category(df, "Супермаркеты")
print(report)
