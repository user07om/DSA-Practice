from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
	"""
		n = length of the array
		first i'th loop iterate over, the array till n - i - 1
		second j'th loop iterate over, the array which has the size of -i-1
		inner condtion checks for the the size of j and j+1
        where j+1 nog overflows because we iterate only i-1
		if condition matched then bigger will throw to the end of array
        so thats why we start inner loop from 0 and 
		end to n-i-1.


        we can add the flag as swapped, in inner loop will add the swapped = True, and outer loop will
        if the flag remain false then whole array is sorted, so no need more iteration over the array!
	"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr



print(bubble_sort([3, 1, 4, 2]))
