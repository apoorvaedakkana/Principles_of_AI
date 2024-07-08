import calendar

def display_calendar(year, month):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_str = cal.formatmonth(year, month)
    print(month_str)

display_calendar(2024, 7)
