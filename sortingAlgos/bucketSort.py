def bucketSort(arr):
    """
    create the empty list within the empty lists.
    add the elements into into the groups of the lists.

    as adding the same category elemetns into that bucket, you hvae to 
    as choosing the idx of buckets.
        - max element from the arr.
        - size variable -> max_ele / len(arr)


    """
    #max element from the variable...
    if len(arr) < 1:
        return arr
    max_ele = max(arr)
    min_ele = min(arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]

    #get the size of the array.
    size = (max_ele-min_ele)/n

    for i in range(n):
        idx = int((arr[i] - min_ele)/size)
        idx = min(idx, n-1)
        print(idx)
        buckets[idx].append(arr[i])

    return buckets

print(bucketSort([]))


#insertion sortalgo for bucket-sort opertaions.
def insert_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def buck_sort_yt(arr: list[int]) -> list[int]:
    n = len(arr)
    buckets = [[] for _ in range(n)]
    max_ele = max(arr)
    result = []

    for i in range(n):
        norm = arr[i] / (max_ele + 1) 
        idx = int(n * norm)
        buckets[idx].append(arr[i])

    for i in range(n):
        result = result + buckets[i]

    max_len = float("-inf")
    rev_buckets= []
    for b in range(len(buckets), 0, -1):
        if len(buckets[b-1]) > max_len:
            rev_buckets.append(buckets[b-1])
    print(rev_buckets, "yoooo fuck yeah")

    res = []
    for b in buckets:
        if len(b):
            res.append(b[0])


    #print(sorted(res))
    print("Answer is here: ", res[:2])

    return buckets

print(buck_sort_yt([1]))


from collections import Counter
def buckets_hash(arr, k):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    freq = Counter(arr)

    if len(arr) <= 1:
        return arr

    print(freq, " fuckkinggggg")
    for key, val in freq.items():
        buckets[val].append(key)

    if len(buckets) <= 1:
        return buckets[0]

    res = []
    for i in range(n-1, 0, -1):
        if buckets[i]:
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

    return res

print("hashmap in bucktes: ", buckets_hash([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))


def sort_char_freq(s: str) -> str:
    freq = Counter(s)

    buckets = [[] for _ in range(len(s)+1)]
    for x, c in freq.items():
        buckets[c].append(x)


    print("most common: ", freq.most_common())

    res = []
    print(buckets)
    for i in range(len(s), 0, -1):
        for ch in buckets[i]:
            res.append(ch*i)

    return "".join(res)


print("answer is sort str: ", sort_char_freq("tree"))


def sliding_window(arr, k):
    #bruteforce approach:
    res = []

    for i in range(len(arr)-k+1):
        for j in range(i, i+k-1):
            print(arr[j], " fucking in")
            if arr[j] < 0:
                res.append(arr[i])
        
        print(arr[i], " fucking")

    return res


print(sliding_window([-8, 2, 3, -6, 1], 2))



