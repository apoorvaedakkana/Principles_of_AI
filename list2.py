
my_list = [1, 2, 3, 4, 5]

another_list = list(range(1, 6))

print("List created using square brackets:", my_list)
print("List created using list() constructor:", another_list)

my_list.append(6)
print("List after adding elements:", my_list)

last_element = my_list.pop()
print("Element popped from list:", last_element)
print("List after pop operation:", my_list)


