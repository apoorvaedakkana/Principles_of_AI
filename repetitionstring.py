def has_duplicate_chars(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False

# Example usage
input_str = "hello"
if has_duplicate_chars(input_str):
    print(f"The string '{input_str}' has duplicate characters.")
else:
    print(f"The string '{input_str}' does not have duplicate characters.")
