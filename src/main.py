import json

from reports import spending_by_category
from utils import load_data
from views import home_page


df = load_data()

home_page_data = json.loads(home_page("2021-12-31 16:44:00", df))
report_data = spending_by_category(df, "Супермаркеты")

result = {
    "home_page": home_page_data,
    "reports": {
        "spending_by_category": report_data,
    },
}

print(json.dumps(result, ensure_ascii=False, indent=4))
