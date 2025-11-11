# is array sorted.
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


print(is_sorted([3, 2, 3]))
print(is_sorted([1, 2, 3]))


def distinct_count(arr):
    return len(set(arr))

print(distinct_count([2, 2, 3, 4]))
print(distinct_count([1, 2, 3, 4]))


def prefix_sum(arr):
    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1]+x)

    return prefix[1:]

print(prefix_sum([2, 3, 4, 5]))

arr = [2, 1, 4]
print(arr[-1])
