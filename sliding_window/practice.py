def maxSum(arr, k):
    windows_sum = sum(arr[:k])
    max_sum = windows_sum
    n = len(arr)
    
    if n < k:
        return None


    for right in range(k, n):
        windows_sum += arr[right] - arr[right-k]
        max_sum = max(max_sum, windows_sum)

    return max_sum


arr_is = [2, 1, 5, 1, 2, 3]
print(maxSum(arr_is, 3))


def mxSum(arr, k):
    i, j = 0, 0
    sum_is = 0
    max_is = 0
    while j < len(arr):   #loop till j reach the end.
        sum_is += arr[j]  #calculate the each index and add it to sum_is variable.
        if j-i+1==k:      #condition for window - if j-i+1 == k (+1 because array as default start with 0)
            max_is = max(max_is, sum_is)  #get the max, with previous sum_is and max_is calculated.
            sum_is -= arr[i]  # remove the i'th element, because we're moving forward.  
            i+=1   #if window size match with k then increament both at same time
            j+=1
        else:
            j+=1   #else window does not match then only move the j index.
    return max_is


print(mxSum(arr_is, 3))



# ---------------------------------------------------------------------------
def sliding_window(arr, k):
    #bruteforce approach:
    res = []

    for i in range(len(arr)-k+1):
        for j in range(i, i+k-1):
            print(arr[j], " fucking in")
            if arr[i] < 0:
                res.append(arr[i])
        
        print(arr[i], " fucking")

    return res


print(sliding_window([-8, 2, 3, -6, 1], 2))

# PRACTICE INTIUITION OF CODE....
# window sum, average, socre over size k. classic the gym warmup of sliding window.
# fixed window - integers.
def max_sum(arr: list[int], k: int) -> int:
    curr_win: int = sum(arr[:k])
    max_win: int = curr_win

    for i in range(k, len(arr)):
        curr_win += arr[i]
        curr_win -= arr[i-k]
        max_win = max(max_win, curr_win)

    return max_win


print(max_sum([3, 4, 1, 9], 2))



#fixed widown - strings.
#examples:
"""
1. max vowels substring of length k 
2. k-length subtring with condition.
3. recolor, flips, character count.
"""
def max_vowels(s: str, k: int):
    vo = set("aeiou")
    count = 0

    for i in range(k):
        if s[i] in vo:
            count += 1

    max_count = count

    for j in range(k, len(s)):
        if s[j] in vo:
            count += 1

        if s[j-k] in vo:
            count -= 1

        max_count = max(max_count, count)

    return max_count

print(max_vowels("soun", 2))


lkjsdf

