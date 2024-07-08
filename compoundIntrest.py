def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + (rate / (n * 100))) ** (n * time)
    return amount

principal = 1000
rate = 5  # in percent
time = 2  # in years
n = 4  # times the interest is compounded per year
amount = calculate_compound_interest(principal, rate, time, n)
interest = amount - principal
print(f"Compound Interest: {interest:.2f}")
