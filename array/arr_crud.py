#-------------------------------------------------------
# ARRAY CRUD OPERATIONS
#-------------------------------------------------------
arr = [1, 2, 3, 4, 5]
print(arr)
#-------------------------------------------------------
# CREATE -> insertion at end, first and at-position.
#-------------------------------------------------------
arr.append(0) #adding the dummy number '0'
for i in range(len(arr)-1, 0, -1):            # it iterate from large to small as i becomes larger.
    arr[i] = arr[i-1]                # ... 
                                    # ...
arr[0] = 2
print(f"inserted at first -> {arr}")

#-------------------------------------------------------

#-------------------------------------------------------
# UPDATE -> update not required to shift element, so we can done by arr.insert(idx, val)
#-------------------------------------------------------
"""
or using iteration: consider - to change the 3rd val to 9val
for i in range(len(arr)):
    if arr[i] == 3:
        arr[i] = 9
        break
"""


#-------------------------------------------------------
# DELETE -> deletion at end, first and at-position.
#-------------------------------------------------------
arr = [1, 2, 3, 4, 5]
print(arr)
"""
using pop() we can delete the last element.
for first position and specific idx and val, we need to iterate over an array.
"""
#--------------deleteion at first position.
for i in range(len(arr)-1):
    arr[i] = arr[i+1]


arr.pop()
print(f"deleted the first index: {arr}")


#-------------deletion at specific position.
idx = 2
for i in range(idx, len(arr)-1):
    arr[i] = arr[i+1]

arr.pop()
print(f"delection at spcific idx {idx}: {arr}")


#--------------deleteion at specific value.
val = 2
pos = 0
for i in range(len(arr)):
    if arr[i] == val:
        pos = i

for i in range(pos, len(arr)-1):
    arr[i] = arr[i+1]

arr.pop()
print(f"deleted the value {val}: {arr}")

#------------------------------------------



#-------------------------------------------------------
# ARRAY CRUD OPERATIONS -- ADVANCE EXAMPLES
#-------------------------------------------------------

#---------------move zero's to the end
arr = [0, 1, 0, 3, 4]
print(f"\nexample arr: {arr}")
# move 0's from arr to the end.
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1

while pos < len(arr):
    arr[pos] = 0
    pos += 1

print(f"moved zero's to the end: {arr}")

#---------------count the frequency of element.
arr = [1, 2, 2, 2, 3]
val = 2
print(f"\ncount the frequency of {val} in {arr}")
count = 0
for i in range(len(arr)):
    if arr[i] == val:
        count += 1

print(f"the frequency of {val} is {count}")



arr = [1, 1, 2, 2, 3, 3] #this works! dublicates in consicutive order.
print(f"\nremove the dublicate elements from an {arr}")
j = 0
for i in range(1, len(arr)):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]

print(f"removed dublicates: {arr[:j+1]}")


#---------------left rotaion by one and also with k.
arr = [1, 2, 3, 4] #output should be -> [2, 3, 4, 1] - rotated by 1.
print(f"\n\nexample array: {arr} rotated by 1")
temp = arr[0]
for i in range(len(arr)-1):
    arr[i] = arr[i+1]
arr[len(arr)-1] = temp
print(f"roated by one: {arr}")

"""
for rotating k'th elements from left we have in wrap above with loop. 
which time complexity becomes O(n*2)
"""
arr = [1, 2, 3, 4, 5, 6] #output should be -> [3, 4, 5, 6, 1, 2] - rotated by k=2.
k = 2
print(f"\nexample array: {arr} and rotaed by {k}")

k = k%len(arr)
for _ in range(k):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp

print(f"rotated arr by k'th: {arr}")

#---------------find largest element | find second largest element.
large_is = float("-inf")
for i in range(len(arr)):
    if arr[i] > large_is:
        large_is = arr[i]

print(f"\nlargest element from an arr is: {large_is}")

#---------

large = float("-inf")
second_large = float("-inf")

for i in range(len(arr)):
    if arr[i] > large:
        second_large = large
        large = arr[i]
    elif arr[i] != large and arr[i] > second_large:
        second_large = arr[i]

print(f"largest: {large} and second largest: {second_large}")


#---------------check is array is sorted!
arr = [1, 2, 4, 3]
flag = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        flag = False

print(f"\nthe given array is sorted or not: {flag}")
        

#---------------linear search + delete element.
arr = [1, 2, 3, 4]
val = 3

pos = -1
for i in range(len(arr)):
    if arr[i] == val:
        pos = i

if pos != -1:
    for i in range(pos, len(arr)-1):
        arr[i] = arr[i+1]

arr.pop()
print(f"\ndelete element by values: {arr}")



#-------------------------------------------------------
# ARRAY CRUD --- ADVANCE QUESTIONS FROM CLAUDE:
#-------------------------------------------------------

#----------------remove all occurences of val.
arr = [1, 2, 3, 2, 4, 2]
arr_old = arr[:]
val = 2

j = 0
for i in range(len(arr)):
    if arr[i] != val:
        arr[j] = arr[i]
        j += 1

n = len(arr)-j
while j < len(arr):
    arr[j] = val
    j += 1

print(f"\nremoved all occurences of {val} from {arr_old} -> {arr[:n]}")

#---------------insert in sorted position.
arr = [1, 3, 5, 7] #output should be [1, 3, 4, 5, 7]
val = 4

pos = 0
for i in range(len(arr)-1):
    if arr[i] < val and arr[i+1] > val:
        pos = i+1
        break

arr.append(0)
for i in range(len(arr)-1, pos, -1):
    arr[i] = arr[i-1]

"""alternate way using if elif else condtion.
but the space complexity is O(n)...
arr_new = [0]*(len(arr)+1)
for i in range(pos, len(arr)-1):
    if i < pos:
        arr_new[i] = arr[i]
    elif arr[i] == val:
        arr_new[pos] = val
    else:
        arr_new[i] = arr[i-1]
"""

arr[pos] = val
print(f"\ninserted {val} in sorted orrder or arr:  {arr}")


#--------------reverse the array without using the extra space.
arr = [1, 2, 3, 4, 5]
old_arr = arr[:]
left = 0
right = len(arr)-1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(f"\n{old_arr} -- orignal array\n{arr} -- reversed array")


#-------------rotate array by right -- anti-clockwise.
# this method time complexity is O(k*n) where k is rotaion and n is arr length
# space complexity is O(1) because it's doing inplace array swaping.
# -- lets try with only one rotation first.
arr = [1, 2, 3, 4, 5]

temp = arr[len(arr)-1]

for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]

arr[0] = temp
print(f"\nlets try with only one rotaion: {arr}")

# -- lets try with k'th right rotaion now.
arr = [1, 2, 3, 4, 5]
k = 2

k = k%len(arr)

for _ in range(k):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

print(f"try with {k}'th right rotaion: {arr}")


#----------------move negative to left and positive elements to the right.
arr = [1, -2, 3, -4, 5] #output should be [-2, -4, 1, 3, 5]

j = 0
for i in range(len(arr)):
    if arr[i] <= 1:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1


#---------------merge to sorted array in sorted order.
arr_one = [1, 3, 6]
arr_two = [2, 4, 5]
o = len(arr_one) #---------len of arr_one
t = len(arr_two) #---------len of arr_two 
res = [0]*(o+t)  #---------new array for merging -- which creates the O(o+t) space comlexity
n = len(res)     #---------len of new array 

i = 0
j = 0
k = 0

#WHILE LOOP SORTED ARRAY MERGING
while j < o and k < t:
    if arr_one[j] < arr_two[k]:
        res[i] = arr_one[j]
        j += 1
    else:
        res[i] = arr_two[k]
        k += 1
    
    i += 1

while j < o:
    res[i] = arr_one[j]
    j += 1
    i += 1

while k < t:
    res[i] = arr_two[k]
    k += 1
    i += 1


#FOR LOOP SORTED ARRAY MERGING -- commented....!
#for i in range(n):
#    if j < o and k < t:
#        if arr_one[j] < arr_two[k]:
#            res[i] = arr_one[j]
#            j += 1
#        else:
#            res[i] = arr_two[k]
#            k += 1
#
#    elif j < o:
#        res[i] = arr_one[j]
#        j += 1
#
#    else:
#        res[i] = arr_two[k]
#        k += 1
#
print(res, "-------------merge sort`")


#---------------remove dublicates from an arr only if an ele is consicutive.
"""
O(n^2) time complexity.
"""
arr = [1, 2, 1, 3, 2, 1] #this not work!
print(arr, "------------old")
count = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)-1):
        if arr[i] == arr[j]:
            arr[j] = arr[j+1]
            count += 1

print(arr[:count-1], "------------new", )


#-------------rotate array, optimal approach O(n) - reverse algorithm
k = 2
arr = [1, 2, 3, 4, 5] # rotate by right (anti-clockwise) e.g. [4, 5, 1, 2, 3]
def reverse_algo(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

k %= len(arr)

#first we have to reverse the entire array - to move the end element to initial level
reverse_algo(arr, 0, len(arr)-1)

#FROM NOW BOTH reverse_algo FUNCTION CALL TO JUST CORRECT THE ORDER OR NUMBERS.
#then we rotate first k'th elements and keep them in correct postion
reverse_algo(arr, 0, k-1)

#now reverse the remaing elements - means keep them in correct numeric order.
reverse_algo(arr, k, len(arr)-1)

print(arr, "right rotaion - clockwise")

arr = [1, 2, 3, 4, 5] # rotate by left (clockwise) e.g. [3, 4, 5, 1, 2]
n = len(arr)
reverse_algo(arr, 0, k-1)
reverse_algo(arr, k, n-1)
reverse_algo(arr, 0, n-1)
print(arr, "left rotaion - anti-clockwise")


#-----------------move all nagative elements to the left of the array.
arr = [1, -2, 3, -4, 5]
print(arr, "orginal array")
j = 0
for i in range(len(arr)):
    if arr[i] < 0:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1
print(arr, "changed array")


#--------------rearrange positive/nagative alternatively.
arr = [1, -2, 3, -4, 5, -6] #output should be -> [1, -2, 3, -4, 5, -6]


#==========================================================================================================================================================

print("==========================================================================================================================================================")
#insert elemet at verious position
# insert at beginning
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
