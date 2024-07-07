def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 23, 45, 70, 11, 15]
target = 70

index = linear_search(arr, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the list")
