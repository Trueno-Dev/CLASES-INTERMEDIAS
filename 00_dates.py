### Dates ###

from datetime import datetime

now = datetime.now()

def print_date (date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2025 = datetime(2025, 1, 1)

print_date(year_2025)
