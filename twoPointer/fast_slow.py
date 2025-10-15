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

    return slow




# REMOVE DUBLICATES.
def rem_dubli(arr: List[int]) -> List[int]:
    if len(arr) == 0: return 0 
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    while len(arr) != i+1:
        arr.pop()

    return arr


print(rem_dubli([1, 2, 2, 3, 4, 4, 5]))

def rem_dubli_var1(arr):
    i = 0
    j = 0
   
    while j < len(arr):
        start = j
        while j < len(arr) and arr[j] == arr[start]:
            j+=1

        if j - start == 1:
            arr[i] = arr[start]
            i+=1

    return i

def inst_val(arr: List[int], val: int) -> List[int]:
    i = 0
    n = len(arr)
    
    while i < n:
        if arr[i] == val:
            arr[i] == arr[n-1]
            n -= 1
        else:
            i += 1

    return n

print("Hey", inst_val([1, 2, 2, 3, 2], 2))


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




