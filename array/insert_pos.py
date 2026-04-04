arr = [1, 2, 3, 4]
n = len(arr)-1
# array.......................... no pythonic way.

#insert at end: arr.append(3)
#insert at beginning or insert at any position
"""
okay, so to insert the value at first index, we have to move all the element to right side and assign the val to first index.

for that we have to append the val first (which will add the val to end of the list then we iterate the arra in reverse order and assign the i+1 as arr[i])
"""
pos = 4
val = 9
if pos == len(arr):
    arr.append(val)
else:
    arr.append(0) #make space in array for our value
    for i in range(n, -1, -1): #iterate in rev order.
        prev_val = arr[pos]
        if i == pos:
            arr[pos] = val
            arr[pos+1] = prev_val
            break
        arr[i+1] = arr[i]

print(arr)

# partition array by condition [e.g. even:odd]
"""
we can achive this by x%2==0 as codition to check but for partitioning we simply iterate over an array the flow is below:
    - get the mid point.
    - insert/assign the value as arr[mid+i or mid-i]
    - if it's even then mid-i
    - if it's odd then mid+i 
"""
arr = [1, 2, 3, 4, 5] #output: [2, 4, 1, 3, 5]
mid = len(arr)//2
read = 0
slow = 0
j = 0
n = len(arr)-1
while read <= n:
    if arr[read]%2 == 0:
        arr[slow] = arr[read]
        slow += 1
    else:
        arr[mid+j] = arr[read]
        j += 1
        if (mid+j) == len(arr): break


    read += 1

print(arr)

j = 0
arr = [1,2,3,4,5]
for i in range(len(arr)):
    if arr[i]%2==0:
        # operation for even number
        arr[j] = arr[i]
        j += 1
        i = j
    else:
        arr[j] = arr[i]
        j += 1

print(arr)



#but here the time complexity is o(n) and space also same as well!
arr = [1, 2, 3, 4, 5, 6, 7, 8]
even = [x for x in arr if x%2==0]
odd = [x for x in arr if x%2!=0]
res = even+odd
print(res, "ohh yeah")

#simple iteration - using the swap variable funciton

arr = [1,2,3,4,5]
apply = 0
for read in range(len(arr)):
    if arr[read]%2==0:
        arr[read], arr[apply] = arr[apply], arr[read]
        apply += 1

print(arr, " ohh of one space complexity")


#two pointer appraoch.
arr = [1,2,3,4,5,6]
even = 0
odd = len(arr)-1
while even < odd:
    while even < odd and arr[even]%2==0:
        even += 1

    while even < odd and arr[odd]%2!=0:
        odd -= 1

    #if even < odd:
    arr[even], arr[odd] = arr[odd], arr[even]



print(arr, " dificult but easy i'd say")



# partition array by condition [e.g. even:odd]


print("just doing the practic")
arr = [1, 2, 3, 4, 5]
pos = 2
val = 9
arr.append(0)
for i in range(len(arr)-2, -1, -1):
    arr[i+1] = arr[i]

    if i == pos or i+1 == pos:
        arr[pos] = val
        break

print(arr)


arr = [1, 2, 3, 4, 5]
arr.append(0)
i = 0
n = len(arr)-1
while i < n and pos != n: 
    #arr[n-i] = arr[n-i-1]
    p = n-i
    n = n-i-1
    arr[n], arr[p] = arr[p], arr[n]
    i += 1
    if n-i-1 == pos:
        arr[pos] = val
        break

arr[pos] = val
print("while loop: ", arr)

arr = [1, 2, 3, 4, 5]
temp = arr[:pos]
temp.append(val)
res = temp+arr[pos:]
print("slicing: ", res)




arr = [1, 2, 3, 4, 5]
arr.append(0)
val = 9
pos = 2
temp = val
for i in range(pos, len(arr)):
    curr_pos = arr[i]
    arr[i] = temp
    temp = curr_pos

print(arr, " something diff")


val = 9; pos = 2
nums = [1, 2, 3, 4, 5]
new = [0]*(len(nums)+1)
for i in range(len(new)):
    if i < pos:
        new[i] = nums[i]
    elif i == pos:
        new[pos] = val 
    else:
        new[i] = nums[i-1]
print(new, "something diff, easy one.")

