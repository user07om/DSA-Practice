


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


#move all zeros to the end: time complexity is O(n) and space is None. O(1)
arr = [0, 1, 1, 0, 2, 1] # [_, _, _, _, 0, 0] non-zero elements order does not matter.

#the bruteforce approach would be -> just remove the zeros and also keep the count. 
#add the zeros as count times in orignal array.

count = arr.count(0)

while 0 in arr:
    key = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            key = i

    for i in range(key, len(arr)-1):
        arr[i] = arr[i+1]

    arr.pop()

for _ in range(count):
    arr.append(0)
print(arr)



# the second approach is array rotation - it's not correct answer bcause as per the problem statement
# we have to keep the order of non-zero elements in order. and in this solution we need to sort an array. So!
arr = [0, 1, 1, 0, 2, 1] # [_, _, _, _, 0, 0] non-zero elements order does not matter.

def rotMoveZero(arr):
    n = len(arr)
    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    if 0 in arr:
        arr.sort()
        count = sum(1 for x in arr if x == 0)

        
        reverse(arr, 0, n-1)#reverse the entire array so the zeros will be pushed to the end.
        reverse(arr, 0, n-count-1)#only reverse the non-zero elements.



    return arr

print(rotMoveZero(arr))


#the only and optimal solution is fast ans slow pointer in two variations: 
# 1. keep the track of 0's as slow poiner and replace it with non-zero element.
# 2. - get the count of non-zero elements.
#    - read the entire array as fast pointer and replace the current element with 0. 
arr = [0, 1, 1, 0, 2, 1] # [_, _, _, _, 0, 0] non-zero elements order does not matter.

def OptiZero(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            #arr[slow], arr[fast] = arr[slow], arr[fast] this is the problem man!
            slow += 1
    return arr

nums = [0, 1, 1, 0, 0, 2]
def OptiZeroTwo(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1

    for i in range(k, len(nums)):
        nums[i] = 0

    return nums

print(OptiZeroTwo(nums))
