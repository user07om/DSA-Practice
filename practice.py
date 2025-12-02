def is_sorted(arr):
    return all(arr[x]<=arr[x+1] for x in range(len(arr)-1))


def distinct_values(arr):
    return len(set(arr))

def prefix_sum(arr):
    prefix = [0]
    for x in arr:
        prefix.append(arr[-1]+x)

    return prefix[1:]

print(prefix_sum([1, 2, 3]))



def two_sum_sorted(arr, t):
    l, r = 0, len(arr)-1 
    while l<r:
        s = arr[l]+arr[r]
        if s == t:
            return True
        elif s < t:
            l += 1
        else:
            r -= 1
    return False

print(two_sum_sorted([2, 3, 4, 5], 7))


def max_in_win(arr, k):
    res = []
    for i in range(len(arr)-k+1):
        res.append(max(arr[i:i+k]))
    return res

print(max_in_win([3, 4, 5, 8, 6, 3], 2))



def max_diff(arr):
    min_val = arr[0]
    max_diff = float('-inf')
    for x in arr[1:]:
        max_diff = max(max_diff, x - min_val)
        min_val = min(min_val, x)

    return max_diff

print(max_diff([7, 1, 5, 3, 0]))

def rot_arr(arr, d):
    """
    time O(n*d) worst case.
    """
    n = len(arr)
    for i in range(d):
        first = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first
    return arr
print(rot_arr([1, 2, 3, 4], 2))

def rot_arr_two(arr, d):
    """
    time linear and space also O(n) by using temp arr
    """
    n = len(arr)
    d %= n
    temp = [0]*n

    for i in range(n-d):
        temp[i] = arr[d+i] 

    for i in range(d):
        temp[n-d+i] = arr[i]

    for i in range(n):
        arr[i] = temp[i]

    return arr
print(rot_arr_two([1, 2, 3, 4], 2))

def rot_arr_three(arr, d):
    """
    using recursion function as reverse
    """
    n = len(arr)
    d %= n

    reverse_a(arr, 0, d-1) #reversing the first d'th ele
    reverse_a(arr, d, n-1) #reversing the d'th to n'th ele
    reverse_a(arr, 0, n-1) #reversing the entire arr

    return arr

def reverse_a(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

print(rot_arr_three([1, 2, 3, 4], 2))
