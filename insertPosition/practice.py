#simple binary search algo practice.

def BSAlgo(arr, x):
    """
    1. first we devide the arr in two half (left and right)
    2. then we pick the mid ele from that array
    3. on besis of that element we search the target value
    4. if the target is less then mid then we remove the first half from the array
    5. wise versa to the right as well - left = mid - 1
    6. and again we split that specifed arr to two sections left/right
    7. the base case is we return the middle element as the target element by comparing!
    """

    left = 0
    right = len(arr) - 1
    while (left<right):
        mid = (left+right)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1


print(BSAlgo([3, 2, 5, 6, 4], 3))