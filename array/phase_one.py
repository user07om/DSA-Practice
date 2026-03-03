#two sum on sorted arrays.
def two_sum(arr: list[int], target: int) -> list[int]:
    left: int = 0
    right: int = len(arr)-1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum > target:
            right -= 1
        else:
            left += 1

    return [0, 0]

print(two_sum([1, 1, 0, 1], 2))


#reverse string
def rev_str(s: str) -> str:
    s = list(s)
    left = 0
    right = len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)

print(rev_str("omkar"))


#valid palindrome
def vali_pali(s: str) -> bool:
    s: list[str] = list(s)
    left: int = 0
    right: int = len(s)-1

    while left < right:
        #check the left char and if it's not alphanumeric then skip(increament) it.
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(vali_pali("rr3"))


#container with most water.
def most_water(arr: list[int]) -> int:
    res: int = 0
    left: int = 0
    right: int = len(arr)-1
    while left < right:
        width = right - left
        height = min(arr[left], arr[right])
        area = width * height
        res = max(res, area)
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1

    return res


print(most_water([1,8,6,2,5,4,8,3,7]))


#three sum...
def three_sum(arr: list[int]):
    arr.sort()  #sorting is important to track the dublicates and skip them 
    n = len(arr)-1
    res = []

    for i in range(n):
        #check the i and it's pre value are same or not if it's same then skip it.
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i+1
        right = n-2
        
        while left < right:

            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum == 0:
                res.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1

                left += 1
                right -= 1
            elif curr_sum < 0:
                right -= 1
            else:
                left += 1



    return res
print("need to work on this: ", three_sum([-1, 0, 1, 2, -1, -4]))


#remove dublicates from sorted array
def rem_dubli(arr: list[int]) -> list[int]:
    if len(arr) < 0:
        return arr

    slow = 0
    for fast in range(len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
        
        arr[slow], arr[fast] = arr[fast], arr[slow]


    return arr

print(rem_dubli([1, 2, 2, 3]))


#max consicutive ones.
def max_cons(arr: list[int]) -> int:
    res = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            res = max(res, count)
            count = 0

    return max(res, count)

print(max_cons([1, 1, 0, 1, 1, 1]))
print(max_cons([1, 0, 1, 1, 0, 1]))





