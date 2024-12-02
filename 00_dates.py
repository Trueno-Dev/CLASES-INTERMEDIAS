### Dates ###

from datetime import datetime, time, date, timedelta
from turtledemo.penrose import start

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

year_2025 = datetime(2025, 1, 1) # Fecha y Hora Manual

print_date(year_2025)

current_time = time(21, 6, 0) # Fecha Manual

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today() # Día Automático.

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 10, 6) # Día Manual

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)