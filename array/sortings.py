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




























class SortingsAlgos:
    def __init__(self, arr):
        self.arr = arr

    def bubbleSort(self):
        n = len(self.arr)
        for i in range(n):
            is_sorted = False
            for j in range(i+1, n):
                if self.arr[i] > self.arr[j]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    is_sorted = True

            if not is_sorted:
                return self.arr

        return self.arr
            
    
    def selectionSort(self):
        n = len(self.arr)
        for i in range(n):
            min_v = i
            for j in range(i+1, n):
                if self.arr[j] < self.arr[min_v]:
                    min_v = j

            self.arr[i], self.arr[min_v] = self.arr[min_v], self.arr[i]

        return self.arr

    def insertionSort(self):
        n = len(self.arr)
        for i in range(n):
            curr = self.arr[i]
            j = i - 1
            while j >= 0 and curr < self.arr[j]:
                self.arr[j+1] = self.arr[j] 
                j -= 1

            self.arr[j+1] = curr


        return self.arr

    def partition(self, arr, left, right):
        piv = arr[right]
        j = left - 1
        for i in range(left, right):
            if arr[i] <= piv:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[j+1], arr[right] = arr[right], arr[j+1]

        return j+1

    def quick_sort(self, arr, left, right):
        if left < right:
            idx = self.partition(self.arr, left, right)
            self.quick_sort(self.arr, left, idx-1)
            self.quick_sort(self.arr, idx+1, right)

        return self.arr

    def qsort(self):
        n = len(self.arr)
        return self.quick_sort(self.arr, 0, n-1)


sorts = SortingsAlgos([2, 3, 1, 4])
#opr = sorts.selectionSort()
#opr = sorts.insertionSort()
opr = sorts.qsort()
print(opr)





























