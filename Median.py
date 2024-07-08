def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median

numbers = [1, 3, 3, 6, 7, 8, 9]
median = find_median(numbers)
print(f"Median of the list: {median}")
