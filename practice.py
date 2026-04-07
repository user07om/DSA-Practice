def v_dif(arr):
    """
    this is use for greedy approach - where it finds the best possible sollution.
    """
    min_v = arr[0]
    max_diff = 0
    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i]-min_v)
        min_v = min(min_v, arr[i])

    return max_diff

print(v_dif([2,3,1,6,4]))
#----------------------------------------

def rot_arr(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]



# -------------------------------------------------------------------------------
#buy and sell stock once and get the max profit through out the day.

def max_profit(prices):
    """
    alternate way would be --
    max_profit = max(max_profit, prices[i] - curr_price)
    curr_price = min(curr_price, prices[i])
    """
    max_profit = float("-inf")
    curr_price = prices[0]
    for i in range(1, len(prices)):
        profit = prices[i] - curr_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < curr_price:
            curr_price = prices[i]

    return max_profit

def max_pro(arr: list[int]) -> int:
    max_profit = float("-inf")
    current = arr[0]
    for i in range(1, len(arr)):
        profit = arr[i] - current
        if profit > max_profit:
            max_profit = profit
        if arr[i] < current:
            current = arr[i]
    return max_profit

print("------------------", max_profit([2, 7, 1, 9, 3]))



def unil_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit
#print("------------------", max_profit([1,4,3,4,5]))

# -------------------------------------------------------------------------------



#array rotations...
"""
there are two types of rations, left and right rotation. exampel = [1, 2, 3, 4, 5]
left rotaion -> [3, 4, 5, 1, 2] -> k=2
right rotaion -> [4, 5, 1, 2, 3] -> k=2

three ways we can implement the rotation array problems...
tempraory array, reversal algorithm and juggling algorithm.
"""

def rev_algo_left(arr: list[int], k: int) -> list[int]: #left rotation (counter clockwise)
    n = len(arr)
    k %= n
    rev_arr(arr, 0, n-1)
    rev_arr(arr, 0, n-k-1)
    rev_arr(arr, n-k, n-1)
    return arr

def rev_algo_right(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k %= n
    rev_arr(arr, 0, n-1)
    rev_arr(arr, 0, k-1)
    rev_arr(arr, k, n-1)
    return arr

def rev_arr(arr: list[int], start: int, stop: int) -> list[int]:
    while start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1

    return arr

print(rev_algo_left([1, 2, 3, 4, 5], 2), "left rotation")
print(rev_algo_right([1, 2, 3, 4, 5], 2), "right rotation")


def temp_algo_left(arr: list[int], k: int) -> list[int]: #left rotaion ([3, 4, 5, 1, 2])
    n = len(arr)
    k %= n
    temp = arr[k:]
    return temp + arr[:k]


def temp_algo_right(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k %= n
    temp = arr[-k:]
    return temp + arr[:-k]
    
print(temp_algo_left([1, 2, 3, 4, 5], 2))
print(temp_algo_right([1, 2, 3, 4, 5], 2))

arr = [1, 2, 3, 4, 5]
k = 2
print(arr[-k:])
print(arr[k:])


def sum_is_k(arr, k):
    seen = set()
    pairs = set()
    for num in arr:
        if k-num in seen:
            pairs.add((num, k-num))
        seen.add(num)

    return pairs 

print(sum_is_k([2, 3, 4, 1, -2, -1], 3))

def sec_larg(arr):
    first = float("-inf")
    second = first

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second

print(sec_larg([2, 4, 1, 2, 3, 5, 3]))
        


def suff_one(arr):
    n = len(arr)
    sufi = [0]*n
    sufi[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        sufi[i] = sufi[i+1] + arr[i]
    
    return sufi

print(f"suffix pattern: {suff_one([1, 2, 3, 4])}")

def pref_one(arr):
    n = len(arr)
    sufi = [0]
    for num in arr:
        sufi.append(sufi[-1]+num)

    return sufi

print(f"prefix pattern: {pref_one([1, 2, 3, 4])}")


def freq_count(arr): 
    freq = {}
    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i], 0)+1

    return freq
print(freq_count([2, 4, 1, 1, 2, 3, 4, 5]))


def equil_idx(arr): #optimal approach time O(n) space O(1)
    rightSum = sum(arr)
    leftSum = 0
    for i in range(len(arr)):
        rightSum -= arr[i]
        if leftSum == rightSum:
            return i

        leftSum += arr[i]

    return -1

print(equil_idx([2, 3, 2, 0, 7, 0]))

def equil_idx_two(arr): #bruteforce approach time O(n*2) and space O(1)
    for i in range(len(arr)):
        left = 0
        right = 0
        for j in range(i):
            left += arr[j]

        for j in range(i+1, len(arr)):
            right += arr[j]
        
        if left == right:
            return i

    return -1

print("brutforce approach: ", equil_idx_two([2, 3, 2, 0, 7, 0]))


def missing_number(arr):
    n = len(arr)
    return n*(n+1)//2 - sum(arr)

print(missing_number([0, 2, 3, 4]))

def miss_num_two(arr): #bruteforce approach or my approach
    n = len(arr)
    min_v = min(arr)
    max_v = max(arr)
    if min_v != 0:
        return 0

    var_is = 0
    count = 1
    while max_v - count in arr:
        count += 1
        var_is = max_v-count

    return max_v+1 if var_is == -1 else var_is

print(miss_num_two([0, 1, 2, 3]))

def miss_num_three(arr): #GPT optimized version.
    arr_set = set(arr)
    max_v = max(arr)

    count = 1
    while max_v - count is arr_set:
        count += 1

    return max_v - count

print("three: ", miss_num_three([0, 1, 2, 3]))

def miss_num_four(arr): #YT approach
    n = len(arr)
    arr_set = set(arr)
    for i in range(n):
        if i not in arr_set:
            return i
    return n

print("four: ", miss_num_four([2, 3, 1, 0]))

def miss_xor_num(arr):
    """
    XOR has some rules:
        - commutative: similar to additin and multiplication left side == right side (sequence not matter)
        - A xor 0 equals to A
        - X xor X equals to 0
    """
    xor_n = 0
    for i in range(len(arr)+1):
        xor_n ^= i

    for x in arr:
        xor_n ^= x

    return xor_n

print("four: ", miss_xor_num([3, 1, 0]))


def has_dubli(arr): #pythonic way
    return len(arr) == len(set(arr))
#print("the following array has dublicate values: ", cont_dubli([1, 2, 2, 3, 4]))

def has_dubli_two(arr): #code
    seen = set()

    for i in range(len(arr)):
        if arr[i] in seen:
            return True

        seen.add(arr[i])

    return False

print("array has dublicate values: ", has_dubli_two([1, 2, 3, 4]))

def get_dubli(arr):
    freq = {}

    for i in range(len(arr)):
        #count the number frequency!
        freq[arr[i]] = freq.get(arr[i], 0)+1

        if freq[arr[i]] and freq[arr[i]] >= 2:
            return arr[i]


    return -1

def get_dubli_effecient(arr): # fast and slow pointer effecint way where fast pointer meet the slow.
    fast = arr[0]
    slow = fast
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

print(get_dubli_effecient([1, 3, 4, 2, 2]))

print(get_dubli_effecient([3, 1, 3, 4, 2]))
print(">>> ", get_dubli_effecient([3, 3, 4, 4, 4, 4, 4, 4]))


def subarrSum(nums, k): #brutforce approach.
    count = 0
    for i in range(len(nums)):
        total_in = 0
        for j in range(i, len(nums)):
            total_in += nums[j]
            if total_in == k:
                count += 1

    return count
            
print("bruteforce approach: ", subarrSum([1, 2, 3], 2))

def subarrSum_Opti(nums, k):
    pref = [0]
    hmap = {}
    count = 0

    for x in nums:
        pref.append(pref[-1]+x)

    for x in pref:
        if x-k in hmap:
            count += hmap.get(x-k)
        hmap[x] = hmap.get(x, 0)+1

    return count


#-----------------------------CRUD OPERATIONS------------------------------
<<<<<<< HEAD
arr = [1, 2, 3, 4]
n = len(arr)
# array.......................... no pythonic way.

#insert at end: arr.append(3)
#insert at beginning


# ---------------------------------------------------------------------------
#-----------------------------TWO POINTERS-----------------------------------
# twoSum sorted, pali and contain most water.
def twoSum(arr: list[int], k: int) -> list[int]:
    left = 0
    right = len(arr)-1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == k:
            return [left, right]
        elif curr_sum > k:
            right -= 1
        else:
            left += 1

    return [0, 0]

print(twoSum([2, 3, 4, 5, 1, 4], 5))

def isPali(s: str) -> bool:
    left: int = 0
    right: int = len(s)-1
    s = s.lower()
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

print(isPali("rac ecar"))


def containerWater(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    res = 0
    while left < right:
        width = right - left
        height = min(arr[left], arr[right])
        area = height * width
        res = max(res, area)
        if arr[left] < arr[right]:
            left += 1
        else: right -= 1

    return res

print(containerWater([0, 1, 2]))


# ---------------------------------------------------------------------------
#-----------------------------SORTING ALGOS OPERATIONS------------------------------
# selection, insertion and bubble sort.
def selectionSort(arr: list[int]):
    for i in range(len(arr)-2):
        min_i: int = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr 

print(selectionSort([5, 4, 3, 2, 1]))

def insertionSort(arr: list[int]):
    for i in range(len(arr)):
        curr: int = arr[i]
        prev: int = i-1
        while prev >= 0 and arr[prev] > curr:
            arr[prev+1] = arr[prev]
            prev -= 1

        arr[prev+1] = curr

    return arr

print(insertionSort([5, 4, 3, 2, 1]))


def bubbleSort(arr: list[int]):
    for i in range(len(arr)):
        is_swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True

        if not is_swapped:
            break

    return arr

print(bubbleSort([5, 4, 3, 2, 1]))

def mergeRec(arr: list[int], start: int, end: int) -> None:
    if start < end:
        mid: int = start + (end - start) // 2
        mergeRec(arr, start, mid)   #left part
        mergeRec(arr, mid+1, end)   #right part
        mergeArr(arr, start, mid, end)

def mergeArr(arr: list[int], start: int, mid: int, end: int) -> list[int]:
    temp = []
    i = start
    j = mid+1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    for i in range(len(temp)):
        arr[i+start] = temp[i]


    
arr = [4, 3, 2, 1]
print(arr)
mergeRec(arr, 0, len(arr)-1)
print(arr)



        
def mostWater(arr: list[int]) -> int: #bruteforce appraoch
    """
    formula is:
    
    """
    for i in range(len(arr)):
        ...

def threeSum(arr: list[int]) -> list[list[int]]:
    n = len(arr)
    res = set()
    for i in range(n-1):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                total = arr[i]+arr[j]+arr[k]
                if total == 0:
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    res.add(triplet)


    print("Yo, ", list(map(list, res)))

threeSum([-1,0,1,2,-1,-4])

def threeSumHash(arr: list[int]) -> list[list[int]]: #hashmap approach
    res = set()

    for i in range(len(arr)):
        seen = set()
        target = -arr[i]

        for j in range(i+1, len(arr)):
            comp = target - arr[j]
            if comp in seen:
                trip = tuple(sorted((arr[i], arr[j], comp)))
                res.add(trip)

            seen.add(arr[j])

    return res

print(threeSumHash([-1, 0, 1, 2, -1, -4]))

def threeSumPointer(arr: list[int]) -> list[list[int]]: #two pointer approach.
    res = []
    arr.sort()

    for i in range(len(arr)):
        left = i+1
        right = len(arr)-1
        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                res.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left+1]:
                    left += 1

                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total > 0:
                left += 1
            else: right -= 1

    return res

print(threeSumPointer([-1, 0, 1, 2, -1, -4]))


def trapingRain(arr: list[int]) -> int:
    res = 0
    left = 0
    right = len(arr)-1

    for i in range(1, len(arr)-1):
        while left < right:
            val = min(arr[left], arr[right]) - arr[i] 
            print(val)
            left += 1
            right -= 1
            res += val

    return res

print(trapingRain([4, 2, 0, 3, 2, 5]))



=======
>>>>>>> a8b1def392eb97d3937765b910395f34e0108df6
