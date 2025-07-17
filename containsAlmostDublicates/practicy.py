def containsAlmostDublicates(arr, indexDiff, valueDiff):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if abs(arr[i]-arr[j]) <= valueDiff and abs(i-j) <= indexDiff:
                return True
    return False