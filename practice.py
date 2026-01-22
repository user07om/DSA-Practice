def rev_arr(arr):
    l, r = 0, len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr

print(rev_arr([1, 2, 3, 4]))
# ---------------------------------------

def v_dif(arr):
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
print(arr[-2:])



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
left rotaion -> [3, 2, 1, 4, 5]
right rotaion -> [4, 5, 1, 2, 3]

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
    rev_arr(arr, 0, k)
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



#-----------------------------CRUD OPERATIONS------------------------------
arr = [1, 2, 3, 4]
n = len(arr)
# array.......................... no pythonic way.

#insert at end: arr.append(3)
#insert at beginning
for i in range(n, 0, -1):
    print(arr[i])




