def calculate_tip(total_bill, tip_percentage):
    tip = total_bill * tip_percentage / 100
    return tip

total_bill = 50.00
tip_percentage = 15
tip = calculate_tip(total_bill, tip_percentage)
print(f"Tip amount: ${tip:.2f}")
