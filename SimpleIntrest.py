def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal = 1000
rate = 5  # in percent
time = 2  # in years
interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: {interest}")
