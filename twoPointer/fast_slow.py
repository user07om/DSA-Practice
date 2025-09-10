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






print(findDubli_two([1, 3, 4, 2, 2, 2]))



#linked list related questions now.


    



