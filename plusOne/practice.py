def plusOne(arr):
    print(arr[-2])
    return arr[:-1] + [arr[-1] + 1]

print(plusOne([1, 2, 3]))