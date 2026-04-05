


print("==========================================================================================================================================================")
# insert elemet at verious position
# insert at beginning
# insert at end
arr = [1, 2, 3, 4, 5]
val = 9
arr.append(0)
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]
arr[0] = val

#insert at position: there are many variations:
arr = [1, 2, 3, 4, 5]
val = 9; idx = 2
arr.append(0)
n = len(arr)

print(arr)
for i in range(n-1, -1, -1):
    arr[i] = arr[i-1]
    if i == idx:
        arr[idx] = val
        break
print(arr)

arr = [1, 2, 3, 4, 5]
arr.append(0)
temp = val
for i in range(idx, len(arr)):
    curr_val = arr[i]
    arr[i] = temp
    temp = curr_val

print(arr)

arr = [1, 2, 3, 4, 5]
new_arr = [0]*(len(arr)+1)
for i in range(len(new_arr)):
    if i < idx:
        new_arr[i] = arr[i]
    elif i == idx:
        new_arr[i] = val
    else:
        new_arr[i] = arr[i-1]

print(new_arr)


print("==========================================================================================================================================================")
# delete first element 
# delete at index
# delete by value

arr = [1, 2, 3, 4, 5]

def delFirst(arr):
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr.pop()
    return arr

def delIndex(arr, idx): #non zero based - means it's start from 0
    for i in range(idx, len(arr)): #if wants zero based, then idx+1..n
        arr[i-1] = arr[i]
    arr.pop()
    return arr

def delValue(arr, val):
    #first get the idx by val checking
    idx = 0
    for i in range(len(arr)):
        if arr[i] == val:
            idx = i

    for i in range(idx+1, len(arr)):
        arr[i-1] = arr[i]
    arr.pop()

    return arr

print(delValue(arr, 2))
