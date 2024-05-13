
fruits = ["apple", "banana"]
print("Initial list:", fruits)


fruits.append("orange")  # Append "orange" to the end of the list
print("After appending 'orange':", fruits)


fruits.insert(1, "grape")  # Insert "grape" at index 1
print("After inserting 'grape' at index 1:", fruits)


fruits.remove("apple")  # Remove the first occurrence of "apple" from the list
print("After removing 'apple':", fruits)


del fruits[0]  # Delete the element at index 0
print("After deleting the element at index 0:", fruits)
