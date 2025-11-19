def sorter(arr):
    n = len(arr)

    low = 0
    mid = 0
    high = n - 1

    while mid <= high:

        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


n = int(input("Size of array: "))
arr = []

for i in range(n):
    val = int(input(f"Enter the value at index {i}: "))
    arr.append(val)

print("Your Array :", arr)
print("Sorted array of 0 1 2:", sorter(arr))
