def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

my_list = [1, 2, 3, 4, 5, 2, 3, 6]  # Example list with duplicates
duplicate_elements = find_duplicates(my_list)
print("Duplicates in the list:", duplicate_elements)
