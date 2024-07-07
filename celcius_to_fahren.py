def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius_temp = 37
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp:.2f} degrees Fahrenheit.")
