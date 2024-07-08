def calculate_total_price(price, tax_rate):
    total_price = price + (price * tax_rate / 100)
    return total_price

price = 100
tax_rate = 8.5
total_price = calculate_total_price(price, tax_rate)
print(f"Total price including tax: ${total_price:.2f}")
