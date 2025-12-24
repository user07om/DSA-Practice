def maxSum(arr, k):
    windows_sum = sum(arr[:k])
    max_sum = windows_sum
    n = len(arr)
    
    if n < k:
        return None


    for right in range(k, n):
        windows_sum += arr[right] - arr[right-k]
        max_sum = max(max_sum, windows_sum)

    return max_sum


arr_is = [2, 1, 5, 1, 2, 3]
print(maxSum(arr_is, 3))


def mxSum(arr, k):
    i, j = 0, 0
    sum_is = 0
    max_is = 0
    while j < len(arr):   #loop till j reach the end.
        sum_is += arr[j]  #calculate the each index and add it to sum_is variable.
        if j-i+1==k:      #condition for window - if j-i+1 == k (+1 because array as default start with 0)
            max_is = max(max_is, sum_is)  #get the max, with previous sum_is and max_is calculated.
            sum_is -= arr[i]  # remove the i'th element, because we're moving forward.  
            i+=1   #if window size match with k then increament both at same time
            j+=1
        else:
            j+=1   #else window does not match then only move the j index.
    return max_is


print(mxSum(arr_is, 3))
