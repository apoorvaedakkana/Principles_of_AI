import datetime

def find_day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = days[date.weekday()]
    return day_of_week

date = datetime.date(2024, 7, 8)
day_of_week = find_day_of_week(date)
print(f"{date} is a {day_of_week}")
