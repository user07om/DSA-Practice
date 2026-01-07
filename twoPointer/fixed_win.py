# Maximum sum of subarray of size k.
def max_sum_sub(arr: list[int], k: int) -> int:
    max_sum = sum(arr[:k])
    curr_sum = max_sum

    for i in range(k, len(arr)):
        curr_sum += arr[i]
        curr_sum -= arr[i-k]
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum

print("maximum sum of subarray: [4, 1, 5, 9, 2]", max_sum_sub([4, 1, 5, 9, 2], 2))


# average of all subarray of size k.
def avg_sub(arr: list[int], k: int) -> list[int]:
    """
    so the avg rule is addition of subarray elements and devide by len.
    """
    res = []
    curr_avg = sum(arr[:k])
    res.append(curr_avg/k)

    for i in range(k, len(arr)):
        curr_avg += arr[i]
        curr_avg -= arr[i-k]
        res.append(curr_avg/k)

    return res

print(f"average of all subarray of size k: {avg_sub([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)}")
print(f"average of all subarray of size k: {avg_sub([1, 2, 3], 1)}")
print(f"average of all subarray of size k: {avg_sub([1, 2, 3], 3)}")



# maximum number of each window of size k
def max_n_of_size(arr: list[int], k: int) -> list[int]:
    """
    so the list/array output contains the subarray of maximum elements
    """
    res = arr[:k]
    curr = res
    for i in range(k, len(arr)):
        if sum(curr) > sum(res):
            res = curr
        curr.append(arr[i])
        curr.remove(arr[i-k])

    return res

print(max_n_of_size([1,3,-1,-3,5,3,6,7], 3))

def win_max_number(arr, k):
    sub_arr = arr[:k]
    res = []
    res.append(max(sub_arr))

    for i in range(k, len(arr)):
        sub_arr.append(arr[i])
        sub_arr.remove(arr[i-k])
        res.append(max(sub_arr))

    return res

print(win_max_number([1,3,-1,-3,5,3,6,7], 3))


#COUNT SUBARRAY OF SIZE K WITH SUM >= X
def count_sum_gt_x(arr, k, x):
    count = 0
    curr_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        curr_sum += arr[i]
        curr_sum -= arr[i-k]
        if curr_sum >= x:
            count += 1

    return count

print(count_sum_gt_x([2, 1, 3, 4, 1], 2, 5))



