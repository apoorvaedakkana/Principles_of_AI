def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count

string = "Hello World"
vowel_count = count_vowels(string)
print(f"Number of vowels in '{string}': {vowel_count}")
