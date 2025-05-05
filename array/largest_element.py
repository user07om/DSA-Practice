# return the largest element from the array.
# brute-force psudo-code.
"""
sort the array in ascending way and return the last element from the array using the slicing methond sorting is done via the sorted methond. the time complexity is O(n) and space is same as well
"""

def lar_ele_sort(arr: list) -> int:
    sort_arr: list = sorted(arr)
    return sort_arr[-1]


"""
using the condition for getting
"""

