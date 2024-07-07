def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
num1 = 10
num2 = 25
num3 = 20

largest = find_largest(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
