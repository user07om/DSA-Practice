#ONE-----------partition array by condition..
#[even]+[odd] array (maintain the relative order)
arr = [8]

j = 0
for i in range(len(arr)):
    if (arr[i] % 2) == 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr, "[even] + [odd] array")



#THREE----------Rotate Array left by k.
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

def rev_arr(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

n = len(arr)-1
rev_arr(arr, 0, n) #reversed the entire array.
print(arr, "reversed the entire array")
rev_arr(arr, 0, n-k)          #reverse
print(arr, "reversed the 0th to ", n-k+1, "elements")
rev_arr(arr, n-k+1, n)
print(arr, "reversed the ", n-k, " to ", n)



#THREE-----------REMOVE DUBLICATES. practice... after 8 hours of break could'nt able to solve this one. MF!
#arr = [1, 2, 3, 3, 2, 1]
#j = len(arr)-1
#val = 3
#for i in range(len(arr)-1, 0, -1):
#    if arr[i] == val:
#        arr[i], arr[j] = arr[j], arr[i]
#        j -= 1
#
#print(arr)
arr = [1, 2, 3, 3, 2, 1]
for i in range(len(arr)):
    for j in range(i+1, len(arr)-1):
        if arr[i] == arr[j]:
            arr[i] = arr[j]
print(arr)


#FOUR-----------FIND ALL PAIRS WITH GIVEN DIFF arr[i] - arr[j] = k
# --- wrap them in set as two pairs of integaer in set and append them in lists.
arr = [1, 5, 3, 4, 2] #OUTPUT: [(3, 1), (4, 2), (5, 3)]
k = 2
uni = set()
res = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)-1):
        if (arr[i] - arr[j]) == k:
            uni.add(arr[i])
            uni.add(arr[j])
            if uni not in res:
                res.append(uni)

print(res)


#FIVE-------------DUTCH NATIONAL FLAG PROBLEM.
arr = [2, 0, 2, 1, 1, 0]

j = 0
for i in range(len(arr)):
    if arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr, "Dutch National Flag")


print("-----------------------------------------------------------------------")
print(
    """
    1. remove all occurences of value 3 from [1, 1, 2, 3, 2, 3, 3, 4, 5]
    2. move zeros to end [0, 1, 0, 3, 12]
    3. remove dublicates from sorted.
    """
)
print("-----------------------------------------------------------------------")
arr = [1, 1, 2, 3, 3, 4, 3, 5]
val = 3

j = 0
for i in range(len(arr)-1):
    if arr[i] != val:
        arr[j] = arr[i]
        j += 1

print(arr)


arr = [0, 1, 0, 3, 12]
slow = 0
for fast in range(len(arr)):
    if arr[fast] != 0:
        arr[slow] = arr[fast]
        slow += 1

for i in range(len(arr)-1, slow-1, -1):
    arr[i] = 0

print(arr[:slow])
print(arr)


arr = [1, 1, 2, 2, 3, 3]
j = 0
for i in range(len(arr)):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]

print(arr, "yoo-------------")


arr = [0, 1, 0, 3, 12]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
print(arr, "fuck -----------")

#TWO----------Find k'th largest element.
arr = [3, 2, 1, 5, 6, 4]
k = 3
"""
THINK: we can iterate the array till k*n and pop the larger element every time, eventually last ele is k'th 
PLAN: 
    iteration _ till len(k)
        max_is is float("-inf")
        iteration i till n
            if arr[i] gt max_is: max_is eq arr[i] 
            pos is i
        arr[pos] is float("-inf")
    return max(arr)
CODE: ---
DEBUG: ---
"""
larger = float("-inf")
pos = 1
for _ in range(k+1):
    for i in range(len(arr)):
        if arr[i] >= larger:
            pos = i
    arr[pos] = float("-inf")


print(max(arr), " it k'th largest element")
print(larger, " it k'th largest element")
print(arr)
