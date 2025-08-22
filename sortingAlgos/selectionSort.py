from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    the selection sort means, it's sort the array by selecting the first elements (i)
    and compare it to inner loop to remaing array except i element/index
    if the condition match thene we just swap that element to min index.

    inner loop, if condition matched then we assign the j'th index to the min_idx variable
    and outer loop we just swap it to the i'th element.
    """
    n: int = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([3, 1, 4, 2]))

