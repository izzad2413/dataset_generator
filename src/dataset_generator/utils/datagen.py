import pandas as pd
import random
from faker import Faker
from io import BytesIO

fake = Faker()

def generate_synthetic_data(schema, num_rows):
    data = {}

    for col in schema:
        col_name = col["name"]
        col_type = col["type"]

        if col_type == "numerical":
            min_val, max_val = col.get("range", (0, 1000))
            data[col_name] = [random.randint(int(min_val), int(max_val)) for _ in range(num_rows)]

        elif col_type == "float":
            min_val, max_val = col.get("range", (0.0, 1000.0))
            data[col_name] = [round(random.uniform(min_val, max_val), 2) for _ in range(num_rows)]

        elif col_type in ["categorical", "ordinal"]:
            values = col.get("values", ["A", "B", "C"])
            data[col_name] = [random.choice(values) for _ in range(num_rows)]

        elif col_type == "date":
            start_date, end_date = col.get("date_range", ("2000-01-01", "2022-12-31"))
            start = pd.to_datetime(start_date)
            end = pd.to_datetime(end_date)
            data[col_name] = [fake.date_between_dates(date_start=start, date_end=end) for _ in range(num_rows)]

    return pd.DataFrame(data)

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='SyntheticData')
    processed_data = output.getvalue()
    return processed_data