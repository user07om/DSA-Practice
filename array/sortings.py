# selection sort:
def sel_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_idx = i #assign the first index to the min_idx
        for j in range(i+1, n): #start the loop from second most element in inner loop
            if arr[j] < arr[min_idx]: #do the comparison does the second element or the min_idx is smaller then the first element.
                min_idx = arr[j]
        #swaping here
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("selection sort: ", sel_sort([2, 1, 4, 3]))


# buble sort
def buble_sort(arr: list) -> list:
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

#print("bubble_ sort: ", buble_sort([2, 1, 4, 3]))


def quick_sort(arr: list) -> list:
    n = len(arr)
    if n <= 0 or n == 1:
        return arr 

    pivot = arr[n//2]
    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]

    return quick_sort(left)+middle+quick_sort(right)


#print("quick sort: ", quick_sort([2, 1, 4, 3]))
