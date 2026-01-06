#Sliding Window
"""
there are two types of sliding window exists. fixed and dynamic variable size.
fixed is given by input variable as k. and dynamic is we have to set the window to get the solution
"""

def sum_sub_arr(arr: list[int], k: int) -> int:
    sum_is = sum(arr[:k])
    max_sum = sum_is

    for i in range(k, len(arr)):
        sum_is = sum_is - arr[k-i] + arr[i]
        if max_sum <= sum_is:
            max_sum = sum_is

    return max_sum

print(sum_sub_arr([4, 2, 9, 1, 8], 2))


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

