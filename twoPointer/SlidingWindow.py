#Sliding Window
"""
there are two types of sliding window exists. fixed and dynamic variable size.
fixed is given by input variable as k. and dynamic is we have to set the window to get the solution
"""

def sum_sub_arr(arr: list[int], k: int) -> int:
    sum_is = sum(arr[:k])
    max_sum = sum_is

    for i in range(k, len(arr)):
        sum_is += arr[k] # add the k'th element e.g second index element
        sum_is -= arr[i-k] # remove the first element - arr[i-k], as 2-2 = 0 where i is 2 idx and k is 2 so
        max_sum = max(max_sum, sum_is)

    return max_sum

print("sum of subarray: ", sum_sub_arr([4, 2, 9, 1, 8], 2))


# Dynamic Window Rule: You use two pointer.
"""
1. left - start of the window.
2. right - end of window
expand with right.
shrink with left.
"""

#exmaple longest subarray sum leq k
def long_subarr(arr, k):
    left = 0
    curr_sum = 0
    max_len = float("-inf")

    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


print("long subarray sum leq k", long_subarr([1, 2, 1, 0, 1, 1, 0], k=4))


#Count Occurences of Anagrams...
#-- first appraoch would be... time-complexity O(n*m) where n = len(s) and m = len(p)
def count_occur_ana(s: str, p: str) -> int: # wrong approach -- what if there are multiple letters?
    k = len(p)
    n = len(s)-k+1
    res = 0

    for i in range(n):
        for j in range(k):
            if p[j] != s[i]:
                res += 1

        res = n - res
        res = res // k

    return res

print(count_occur_ana("foryxoxoxoxoortorrofls", "for"))

#-- sliding window approach would be... 
def count_occur_win(s: str, p: str) -> int:
    ...



# --longst substring without repeating the characters.
"""
longest substring without repeating the characters.
 - abcabca -> abc is the answer. is the substring -> which is contiguise characters.
 - aca -> is not the answer cause it's the subsequece.
"""
def long_sub(s: str) -> int:
    max_len = 0
    curr_len = 0
    seen = set()

    for i in range(len(s)):
        seen.add(s[i])
        for j in range(i+1, len(s)):
            if s[j] in seen: 
                seen.remove(s[i])
                break

            curr_len = j-i+1
            seen.add(s[j])

        max_len = max(max_len, curr_len)

    return max_len




print(long_sub("abcabcbb"), "fuck")
print(long_sub("pwwkew"), "fuck")
print(long_sub("dvdf"), "fuck ----")




#best time to buy and sell stocks.
def best_time(prices: list[int]) -> int:
    ...
