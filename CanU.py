#find max.
#count char.
#is sorted.
#reverse string.
from typing import List

def find_max(arr: List[int]) -> int: 
    #took 30minutes. to try both apporach, first one easy second is little hard.
    max_is = arr[0]
    left, right = 0, len(arr)-1
    #for i in range(len(arr)):
        #if arr[i] >= max_is:
            #max_is = arr[i]
    """
    input: arr[3, 1, 5], output: max=?
    using two-pointers appraoch, at opposite pointer!
    loop till left < right:
    get the max between two pointers.
    increament the left by one, if max value less 
    else right decreament by one if value bigger.
    
    """
    max_is = arr[0]
    while left < right:
        max_is = max(arr[left], arr[right])
        left += 1
        right -= 1
    return max_is

print(find_max([3, 90, 4, 5]))



def count_char(s, t):
   #total time take to solve 20minutes. at first trying with hashMap.
   #if i store every char in hashMap then at the end just return it's value, but could not solve through it
    count = 0
    for i in range(len(s)):
        if t == s[i]:
            count += 1

    return count

print(count_char("hellollll", 'l'))


def is_sorted(arr: List[int]) -> bool: 
    #it took me almos 20minutes, first i'm reversing the array i dont know whay
    #return arr[:] == arr[::-1]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                return False
        
    return True

print(is_sorted([1, 2, 3]))


def rev_str(s: str) -> str:
    #python makes life easy, but if no python then second apporach is my

    #return s[::-1]

    #i dont know how can i solve with two arrays, (bubblw sort)
    #for i in range(len(s)):
        #for j in range(i+1, len(s)):
            #if s[i]

    
    #two pointer appraoch, lets see.
    s = list(s)
    left, right = 0, len(s)-1 #30 minutes.
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
    #its failing. i cannot troublshoot it, i think i should add the condition somewhere 

print(rev_str("omkar"))
