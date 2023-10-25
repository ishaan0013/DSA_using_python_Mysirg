from array import *
arr = array("l", [12, 42, 45, -67, 24, 65, 10])

for i in range(len(arr)):
    idx = 0
    while (idx < (len(arr)-1)):
        if (arr[idx] > arr[idx+1]):
            arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        idx += 1

print(arr)
