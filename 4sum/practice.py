
# four sum - 
def four_sum(arr, t):   #bruteforce way.....
    rus = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == t:
                        rus.append([arr[i], arr[j], arr[k], arr[l]])

    return rus




print(four_sum([1, 0, -1, 0, -2, 2], 0))