

## it is question find how many number of the freq coming

def duplicate_finder(arr):
    n = len(arr)
    
    freq = {}

    for arr in arr:
        if arr in freq:
            freq[arr] += 1
        else:
            freq[arr] = 1


    count = 0
    for key in freq:
        if freq[key] == 2:
            count += 1

    return -1 if count == 0 else count




n = int(input("Array size: "))
arr = []

for i in range(n):
    val = int(input(f"Enter the value {i} index: "))
    arr.append(val)


print("array ready to find multiple: ", arr)

multiple_dup = duplicate_finder(arr)

if multiple_dup != -1:
    print("Find Multiple Duplicate Count: ",multiple_dup)

else:
    print("No Multiple Duplicate Find")