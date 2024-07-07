def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    # Check if the string equals its reverse
    return s == s[::-1]

# Example usage
input_str = "A man a plan a canal Panama"
if is_palindrome(input_str):
    print(f"The string '{input_str}' is a palindrome.")
else:
    print(f"The string '{input_str}' is not a palindrome.")
