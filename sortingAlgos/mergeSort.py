def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right-left) //2    #this is becasue, interger value not overflow.
        mergeSort(arr, left, mid)        #left part of the array
        mergeSort(arr, mid+1, right)     #right part of the array

        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    i = left; j = mid+1
    temp = []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for i in range(len(temp)):
        arr[i+left] = temp[i]


arr = [2,1,3]
mergeSort(arr, 0, len(arr)-1)
print(arr)


        
        
