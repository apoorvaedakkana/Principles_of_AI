def lcm(x, y):
    # Find the greater number
    if x > y:
        greater = x
    else:
        greater = y
    
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    
    return lcm

# Example usage
num1 = 24
num2 = 36
result_lcm = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result_lcm}")
