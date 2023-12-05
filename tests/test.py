import pydate_generator
from datetime import date

start = date(2023, 12, 23)
end = date(2024, 1, 5)

for date in gen_dates(start, end):
    print(date)
