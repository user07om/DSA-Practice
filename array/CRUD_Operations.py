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

arr = [1, 2, 3, 4, 5]; val = 2
def delValue(arr, val):
    #first get the idx by val checking
    idx = 0
    for i in range(len(arr)):
        if arr[i] == val:
            idx = i

    for i in range(idx, len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()

    return arr

print(delValue([1, 2, 3, 4, 5], 2), "yoo--------------------")


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

print([0, 1, 2, 0], "does it make sense, this won't work.")

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
            arr[fast], arr[slow] = arr[slow], arr[fast]
            #arr[slow], arr[fast] = arr[slow], arr[fast] this is the problem man!
            slow += 1
    return arr
print(OptiZero(arr), "Fuck it")

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

arr = [1,2,3,2,4,2]; k = 2

def remOccur(arr, k):
    n = len(arr)
    s = 0
    for i in range(n-1):
        if arr[i] != k:
            arr[s] = arr[i]
            s += 1

    return arr[:s]

print(remOccur(arr, k), "yoo------------------remoccr--")


arr = [1,1,2,2,3,3]
def remDubli(arr):
    n = len(arr)
    u = 0
    for r in range(n-1):
        if arr[r] != arr[u]:
            u += 1
            arr[u] = arr[r]

    for i in range(u+1):
        arr.pop()

    return arr

print(remDubli(arr), "yoo------------------remdubli--")

arr = [1,-2,3,-4,5]
def isSap(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] >= 0 and arr[i+1] < 0:
            count += 1
    if count > 1: 
        return False
    return True

def mvNgLeft(arr):
    n = len(arr)
    for i in range(len(arr)-1):
        if arr[i] < 0:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    #mvNgLeft(arr)
    if not isSap(arr): 
        mvNgLeft(arr)
    
    return arr


arr = [1, -2, 3, -4, 5]
def moveNeg(arr): #fast and slow pointer.
    n = len(arr)
    s = 0
    for i in range(n):
        if arr[i] >= 0:
            arr[i], arr[s] = arr[s], arr[i]
            s += 1

    return arr
print(moveNeg(arr), "fuck it")

arr = [1, -2, 3, -4, 5]
def mvNeg(arr): #two opposite pointers.
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] >= 0:
            left += 1
        elif arr[right] < 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

print(mvNeg(arr), "yooo")



def secLarge(arr):
    large = arr[0]
    sec_large = large
    for x in arr:
        if large > x > sec_large:
            sec_large = x
        elif x > large:
            sec_large = large
            large = x

    return large, sec_large

print(secLarge([1, 2, 3, 4]))

arr = [4, 9, 1, 5, 6, 8]; k=3
def kthLargest(arr, k):
    for _ in range(k-1):
        max_v = arr[0]
        key = 0
        for i in range(len(arr)):
            if arr[i] > max_v:
                max_v = arr[i]
                key = i
        
        arr.pop(key)


    return max(arr)


print(kthLargest(arr, k), "kth largest")


def countFreq(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0)+1

    return freq

def cFreqTwo(arr):
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    return freq

print(cFreqTwo([1, 1, 2, 2, 3, 3, 3, 4]))

def isSorted(arr):
    sort_flag = True
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            sort_flag = False

    return sort_flag

print(isSorted([1, 3, 5, 4]))

#def mergeArr(arr1, arr2):
    #i = 0
    #j = 0


#num1 = [1, 2, 3]; num2 = [1, 2, 3, 4, 5]
#if len(num1) > len(num2): n = len(num1)
#else: n = len(num2)
#print(n)


#arr = [1, 2, 3, 4] # Output: [1, 3, 6, 10]
#res = []
#for i in range(len(arr)+1):
    #res.append(sum(arr[:i]))
#print(res)

arr = [1, 2, 3, 4] # Output: [1, 3, 6, 10]
inputArr = [1, 2, 3, 4]
def prefSum(arr):
    arr.append(0)
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = 0

    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]

    return arr

def rangeSum(pre, left, right):
    rightSum = pre[right]
    leftSum = pre[left] if left > 0 else 0
    return rightSum - leftSum

def targetSum(arr, target):
    left = 0
    right = len(arr)-1
    ans = []
    while left < right:
        total = arr[right] - arr[left]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            ans = inputArr[left:right]
            left += 1
            right -= 1


    return ans

prefSum(arr)
print(arr, inputArr)
print(rangeSum(arr, -1, 2))
print(targetSum(arr, 6))


arr = [5, 4, -1, 7, 8]
#arr = [1, 2, 3, 4, 5]
max_v = float("-inf")
for i in range(len(arr)):
    for j in range(i, len(arr)+1):
        for k in range(i, j):
            #res.append(sum(arr[i:j]))
            print(arr[k], end=" ")
        print(" -- ", sum(arr[i:j]))
        if sum(arr[i:j]) > max_v:
            max_v = sum(arr[i:j])
    print()


print(max_v, "---------------------------------------------------")


def equiIdx(arr):
    ans = -1
    for i in range(1, len(arr)-1):
        is_valid = sum(arr[:i]) == sum(arr[i+1:])
        if is_valid:
            ans = i
            break

    return arr[ans]

print(equiIdx([3, 1, 5, 2, 2]))
arr = [3, 1, 5, 2, 2]
def equilibreumIdx(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]


equilibreumIdx(arr)
print(arr)
    


def validPali(s):
    s = s.lower()
    l = 0
    r = len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1

        while l < r and not s[r].isalnum():
            r -= 1

        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True


print(validPali("A man, a plan, a canal: Panama"))


arr = [-4,-1,0,3,10] 
res = []
def SquarSort(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        if abs(arr[left]**2) > abs(arr[right]**2):
            res.append(abs(arr[left]**2))
            left += 1
        else:
            res.append(abs(arr[right]**2))
            right -= 1

    return res

print(SquarSort(arr))


arr = [1, 1, 1, 2, 2, 3, 3]
def remDubliCates(arr):
    slow = 2
    for fast in range(2, len(arr)):
        if arr[fast] != arr[slow-2]:
            arr[slow] = arr[fast]
            slow +=1

    return arr[:slow]
print(remDubliCates(arr))

res = []
def remDubliBrute(arr): #bruteforce approach:
    res.append(arr[0])
    res.append(arr[1])

    prev = 1
    for read in range(2, len(arr)):
        while arr[read] != arr[prev]:
            res.append(read)
            prev = read 
        
        continue


    return res
print(remDubliBrute(arr), "something is wrong!")
