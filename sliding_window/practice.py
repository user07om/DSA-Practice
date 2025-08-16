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
    while j < len(arr):
        sum_is += arr[j]
        if j-i+1==k:
            max_is = max(sum_is, sum_is)
            sum_is -= arr[i]
            i+=1
            j+=1
        else:
            j+=1
    return max_is


print(mxSum(arr_is, 3))
