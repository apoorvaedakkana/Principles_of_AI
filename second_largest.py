def find_second_largest(numbers):
    numbers = list(set(numbers))  # Remove duplicates
    numbers.sort(reverse=True)
    return numbers[1] if len(numbers) > 1 else None

numbers = [10, 20, 4, 45, 99, 20]
second_largest = find_second_largest(numbers)
print(f"Second largest number: {second_largest}")
