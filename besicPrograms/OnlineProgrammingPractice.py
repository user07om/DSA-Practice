
arr = [22, 1, 2, 3, 4, 5, 6, 7]
index = 3
n = len(arr)
value = 11

print(arr)
# arr.insert(1, 11)
# print(arr)

# arr.append(None)
# for i in range(n, index, -1):
#     print(arr[i])
#     arr[i] = arr[i-1] 
#     print(arr[i], "----------")
# # arr[index] = value
# print(arr)

# i want to remove the element now, so 
"""
rem_ele = 0
iterate and starts at index to len(arr)-1.
    - assign the current elements as i, to i+1.
"""

for i in range(index, n-1):
    arr[i] = arr[i+1]
arr.pop()
print(arr)

# max and min value.
"""
assign first index to the max or min as assume it's the max/min value
    - iterate over the arr
    - condition is curr ele bigger then assume value
    - if condition match then assing the current ele to variable
    - else continue till the end.
"""
max_v = arr[0]
for x in arr:
    if x > max_v:
        max_v = x
print(max_v)


# reverse arr.

"""
there are many reverse inbuild fucntions -- .reverse() in memeroy and
slicing method which creates the new array. [::-1]. lets try not
pythonic way to reverse the array.
initialize two variables left and right.
assign 0 to left and len(arr)-1 to the right.
    - loop til left is less then right - while loop
    - swap the left with right and right with left.
    - in loop increase the left by one 
    - and decrease the right by one.
"""

left = 0
right = len(arr)-1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)

# -----------------
"""
serach target in arr and return it's index. the pythonic approach
would be below given.
if target in arr:
    index = arr.index(target)
    
the non-pythonic way is, iterate over the arr
    - if current element equal to target
    - return it's index else return -1
"""
target = 2
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
        break
    continue


"""
binary search -- array must be sorted then the time complexity will
be logn else the time complexity increases.
    - initialize left and right variables and assign 0 and n-1
    - while left <= right (== to because we check till ends)
    - get the mid of array by adding left+right//2
    - if arr[mid] == target: return mid
    - elif arr[mid] greater than target: right -= 1
    - elif arr[mid] lesser than target: left += 1
"""
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

print(binary_search([1, 2, 3, 4], 2))

# ----- Bubble sort
"""
bubble sort is just way to sort the array by swaping the elements
    - time complexity is - O(n2)
    - uses two loops - outer loop for iterating over the arr
    - inner loop till n-1-i (i because each iteration the inner loop will reduce the size of arr`)
    - the condition inside the loop will check is current i is great
    er than it's next (i+1) element.
    - if then swap the value to next element.
    
"""
arr = [4, 6, 8, 2, 1]
print(arr, "non sorted way")

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr, "sorted way")


# ---- selection sort
"""
the selection sort is finding the elements min_idx, mean 
    - iterate over the arr
    - in loop - condition curr_ele is less-then min_idx val.
    - assignt he min_idx = i
    - if yes, then assign the curr_ele idx to min_idx
    - out of condition swap those variables to current indx.
"""



# COMMON ARRAY PATTERNS. 
# two pointers  --- opposite and slow and fast.
#opposite pointers ---
"""
same algo used in reverse array.
assign two variables left and right.
left is 0 and right is len(arr)-1
while loop till left < right: left+=1 and right-=1
"""

#slow and fast pointers --
"""
initialize the slow variable as 0, 
iterate over the array as fast pointer till len(arr)
if certain coditin match then increament the slow by one.
"""


# there are two types of sliding window patterns.
# fixed size and variable size.

"""
find the ave of sum of max subarray.
"""

arr = [1, 3, 2, 6, 1]
k = 2
win_sum = sum(arr[:k])
max_sum = win_sum
# sum_avg = 0
# for i in range(len(arr)):
#     sum += arr[i]
#     for j in range(k, len(arr)-k):
#         sum -= arr[i]
#         sum += arr[j]
#     result = max(result, sum)
    
# print(result/k)
for i in range(k, len(arr)):
    win_sum += arr[i]
    win_sum -= arr[i-k]
    print(f"{i} --> {arr[i], arr[i-k]} what is {i}-{k} {i-k}")
    max_sum = max(max_sum, win_sum)

print(max_sum, win_sum)
    





# -- selection sort.
"""
iteration over the array
    - declare the variable min_idx and assing i to it as pre element
    - inner loop - from i+1 to n, because it's the comparison sort so left subarray is sorted and we have to check from unsosrted (right side) and compare it with i+1 means left end element (right side of sorted subarray)
    - inner loop the condition - if j'th ele is lesser than min_idx element then we have to assign the j idx to min_idx var 
    - in outer loop we have to swap the i to min_idx.
"""
arr = [3, 1, 5, 2]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)


# -- Insertin Sort.
"""
"""
arr = [3, 1, 2, 5]
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1       # arrign the prev val to j.
    while j >= 0 and arr[j] > key:  # condn and loop till and pre ele is greater then curr ele.
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print(arr)


# -- Prefix Sum..
"""
effecient and ease the repetative task that takes time.
 - preprocessing thats why called prefix (preprocess function)
"""
curr = 0
dumm_arr = []
for i in range(len(arr)):
    curr += arr[i]
    dumm_arr.append(curr)
print(dumm_arr)

prefix = [0] * (len(arr)+1)
for i in range(len(arr)):
    prefix[i+1] = prefix[i] + arr[i]
print(prefix, "yeah")

# 
    
    




