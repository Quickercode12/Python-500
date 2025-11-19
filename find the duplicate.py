## it is question only to find single check element

def duplicate_value_finder(arr):

  
    n = len(arr)   ## findig the size of the array

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return arr[i]
            else:
                continue

    return -1


n = int(input("size of arr: "))   ## user size input
arr = []  ## empty decide array

for i in range(n):    ## loop to take value to user input to put into array
    val = int(input(f"Enter index {i}:"))
    arr.append(val) ## append val in arr

print("Array ready:",arr)   ## ready to find duplicate value

duplicate_value = duplicate_value_finder(arr)   ## calling function holding duplicate value

## function if else condition
if duplicate_value != -1:
    print("duplicate value in array:",duplicate_value)    

else:
    print("duplicate value not presented")