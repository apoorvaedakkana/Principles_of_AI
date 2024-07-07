def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

my_list = [1, 2, 3, 4, 5, 2]  # Example list with duplicates
if has_duplicates(my_list):
    print("List contains duplicates.")
else:
    print("List does not contain duplicates.")
