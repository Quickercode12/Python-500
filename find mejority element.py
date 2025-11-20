from collections import Counter

def finder_majority(arr):
    n = len(arr)

    freq = Counter(arr)

    for key, value in freq.items():
        if value > n // 2:
            return key

    return -1


n = int(input("size of the array: "))
arr = []

for i in range(n):
    val = int(input(f"enter value at index {i}: "))
    arr.append(val)

print(f"Your array: {arr}")

majority_element = finder_majority(arr)

if majority_element != -1:
    print(f"Majority element is {majority_element}")
else:
    print("Majority element not found (-1)")
