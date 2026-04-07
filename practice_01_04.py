#sorting algos (bubble, selection, insertion and merge sort)

def bubbleSort(arr: list[int]) -> list[int]:
    n: int = len(arr)
    for i in range(n):
        is_swapped: bool = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True

        if not is_swapped:
            break

    return arr

print(bubbleSort([4,3,2,1]))


def selectionSort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        key = i
        for j in range(i+1, n):
            if arr[key] > arr[j]:
                key = j

        arr[i], arr[key] = arr[key], arr[i]

    return arr

print(selectionSort([3,2,1]))

def insertionSort(arr: list[int]) -> list[int]:
    n: int = len(arr)
    for i in range(n):
        min_i = i-1
        curr = arr[i]
        while min_i >= 0 and arr[min_i] >= curr:
            arr[min_i+1] = arr[min_i]
            min_i -= 1

        arr[min_i+1] = curr

    return arr

print(insertionSort([5,4,3,2,1]))


def mergeSort(arr: list[int], start: int, end: int) -> None:
    if start < end:
        mid = start + (end-start)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        mergeArr(arr, start, mid, end)


def mergeArr(arr, start, mid, end) -> list[int]:
    i = start
    j = mid
    temp = []
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j -= 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j -= 1


    for i in range(len(arr)-1):
        arr[i+start] = temp[i]
        

arr = [3,2,1]
#print(mergeSort(arr, 0, len(arr)-1))
#print(arr)



def twoSum(arr: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(arr)):
        total = target - arr[i]
        if total in seen:
            return [seen[total], i]
        seen[arr[i]] = i

    return [0, 0]

print(twoSum([2, 7, 11, 15], 9))

def twoSum2(arr: list[int], target: int) -> list[int]:
    p = 0
    q = len(arr)-1
    while p < q:
        total = arr[p] + arr[q]
        if total > target:
            q -= 1
        elif total < target:
            p += 1
        else:
            return [p+1, q+1]

    return [0, 0]

print(twoSum2([2, 7, 11, 15], 9))

def threeSum(arr: list[int]) -> list[list[int]]:
    arr.sort() #array must be sorted.
    res = []
    for i in range(len(arr)):
        #skiping dublicates of i.
        if i > 0 and arr[i] == arr[i-1]:
            continue

        p = i+1
        q = len(arr)-1
        while p < q:
            total = arr[i]+arr[p]+arr[q]
            if total > 0:
                q -= 1
            elif total < 0:
                p += 1
            else:
                res.append([arr[i], arr[p], arr[q]])
                p += 1
                q -= 1

                while p > q and arr[p] == arr[p-1]:
                    p += 1

                while p > q and arr[q] == arr[q+1]:
                    q -= 1


    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))



def containerWater(arr: list[int]) -> int:
    res = 0
    p = 0
    q = len(arr)-1
    while p < q:
        width = q - p
        height = min(arr[p], arr[q])
        area = width * height
        res = max(res, area)

        if arr[p] < arr[q]: #from smalled heigh the water will overflow, so we have to call it inward!p += 1
            p += 1
        else: q -= 1

    return res

print(containerWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        

def validPali(s: str) -> bool:
    sent = "".join(c.lower() for c in s if c.isalnum())
    return sent == sent[::-1]

print(validPali("omkar"))
