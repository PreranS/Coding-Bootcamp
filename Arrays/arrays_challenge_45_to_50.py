# Coding Challenges 51–54 : Sort and Search Arrays

# Level 0: Accept array elements
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

print("\nOriginal Array:", arr)

# Level 1: Reverse the array
reversed_arr = []
for i in range(n - 1, -1, -1):
    reversed_arr.append(arr[i])

print("Reversed Array:", reversed_arr)

# Level 2: Sort the array (Ascending or Descending)
order = input("Enter sorting order (A for Ascending / D for Descending): ").upper()

sorted_arr = arr.copy()

for i in range(n):
    for j in range(i + 1, n):
        if order == 'A':
            if sorted_arr[i] > sorted_arr[j]:
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
        elif order == 'D':
            if sorted_arr[i] < sorted_arr[j]:
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]

print("Sorted Array:", sorted_arr)

# Level 3: Binary Search (works on sorted array)
search = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if sorted_arr[mid] == search:
        found = True
        break
    elif sorted_arr[mid] < search:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Element found at position:", mid)
else:
    print("Element not found")
