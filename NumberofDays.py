from datetime import date

def days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days

date1 = date(2024, 1, 1)
date2 = date(2024, 7, 8)
days = days_between_dates(date1, date2)
print(f"Days between {date1} and {date2}: {days}")
