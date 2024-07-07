def count_letters(s):
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count

# Example usage
s = "Hello, World! 123"
letter_count = count_letters(s)
print(f"The number of letters in the string is: {letter_count}")
