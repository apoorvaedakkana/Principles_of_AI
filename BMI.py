def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = 70  # in kilograms
height = 1.75  # in meters
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f}")
