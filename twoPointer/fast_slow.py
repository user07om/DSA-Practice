from typing import List

def findDubli(arr: List[int]) -> int:
    slow = arr[0]
    fast = arr[arr[0]]

    #Phase 1: THIS LOOP FOR DETECTING THE CYCLE.
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
        print("phase one: ", slow, fast)

    #Phase 2: FIND CYCLE START [DUBLI NUMBER]
    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
        print("phase two: ", slow, fast)

    return slow

def findDubli_two(arr: List[int]) -> int:
    """
    it will not work - the second approach required to find the entry point of dulbicate value.
    """
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        print("phase one: ", slow, fast)
        if slow == fast:
            break

    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]


    return slow




# REMOVE DUBLICATES.
def rem_dubli(arr: List[int]) -> List[int]:
    if len(arr) == 0: return 0 
    slow = 0
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]

    return arr[:slow]


print(rem_dubli([1, 2, 2, 3, 4, 4, 5]), "hey lets see")

def rem_dubli_var1(arr):
    slow = 0
    fast = 0
   
    while fast < len(arr):
        start = fast
        while fast < len(arr) and arr[fast] == arr[start]:
            fast+=1

        if fast - start == 1:
            arr[slow] = arr[start]
            slow+=1

    return slow

def inst_val(arr: List[int], val: int) -> List[int]:
    slow = 0
    n = len(arr)
    
    while slow < n:
        if arr[slow] == val:
            arr[slow] == arr[n-1]
            n -= 1
        else:
            slow += 1

    return n

print("Hey", inst_val([1, 2, 2, 3, 2, 1], 2))


def lets_see(arr, val):
    i = 0
    for j in range(len(arr)):
        if arr[j] != val:
            arr[i] = arr[j]
            i += 1

    del arr[i:]
    
    return arr

print(lets_see([1, 2, 2, 3, 3], 2))

def move_zero(arr):
    i = 0;
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return arr

print(move_zero([2, 3, 0, 2, 0, 3]))












# -----------------------------------
#lets do coding here.

"""
what does fast and slow pointers mean.
    - the default fast is similar to i'th iteration.
    - the slow pointer means it's the j but it's only
    iterate when certain condition match.
psudo code for fast and slow pointer.
    iteration over the array as fast.
        #do some work here.
        condition met:
            incraament the slow pointer by one.
        outer loop as fast pointer will contnenue it's iteration.
"""

#remove dublicates and move zeros to the end.

def remove_dubli(arr: list[int]) -> int:
    slow = 0
    for fast in range(1, len(arr)):
        # some work here
        if arr[fast] != 0:
            slow += 1
            arr[slow] = arr[fast]

    return slow+1

arr = [2, 1, 0, 1, 3, 0, 2]
new_len = remove_dubli(arr)
print(arr[:new_len], "hey yoo")



#move zeros to the end.
def move_zero_to_end(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    slow = 0 
    for fast in range(1, len(arr)):
        if arr[fast] != 0:
            arr[fast], arr[slow] = arr[slow], arr[fast]
            slow += 1

    return arr

print(move_zero_to_end([0, 1, 0, 3]))


















