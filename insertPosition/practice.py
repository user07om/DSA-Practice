#simple binary search algo practice.

def BSAlgo(arr, target):
    """
    1. first we devide the arr in two half (left and right)
    2. adding left and right and round up to get the mid.
    3. if the mid is equal to x then return the mid.
    4. if the arr[mid] as arr element of that indices is smaller that x, then assing the mid to rigth and decreament by 1.
    5. if the arr[mid] as arr element of that indices is greater than x, then assign the mid to left and indrease by 1
    6. then it round of that left and right and get the mid again.
    """
    left, right = 0, len(arr)-1
    result = 0
    while (left<right):
        mid = (left+right)//2
        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return result

print(BSAlgo([2, 4, 6, 8, 10], 3))