def convert_minutes_to_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

minutes = 130
hours, remaining_minutes = convert_minutes_to_hours(minutes)
print(f"{minutes} minutes is {hours} hours and {remaining_minutes} minutes")
