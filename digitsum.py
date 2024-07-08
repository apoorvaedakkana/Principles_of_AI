def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

number = 12345
digit_sum = sum_of_digits(number)
print(f"Sum of digits of {number}: {digit_sum}")
