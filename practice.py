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

#print("------------------", max_profit([7,1,5,3,6,4]))


def unil_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit
#print("------------------", max_profit([1,4,3,4,5]))

# -------------------------------------------------------------------------------






