"""
Classic questions for opposite questions.
- finding pairs with target to sum in sorted array.
- palindrom
- container with most water.
"""

# finding pair with most water is simplest
def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    """
    as opposite pointers/ref we have to add those two and compare with the target
    if it's equal then return it's idx else default [0, 0]
    """
    left: int = 0
    right: int = len(arr)-1
    while left < right:
        total_sum: int = arr[left]+arr[right]
        if total_sum == target:
            return [left, right]
        elif total_sum < target:
            left += 1
        else:
            right -= 1

    return [0, 0]



# check is given sentex pali or not?
def isPali(s: str) -> bool:
    """
    Input: s
    Output: bool 
    Method: used two pointes opposite pattern - 
        - if the character isalnum() and equal left == right then continue
        - if the left is qual to not isalnum() then decrease it by one
        - same for the rigth if it's not isalnum() then increase it by one
    """
    s = s.lower()
    if len(s) <= 1:
        return True

    left: int = 0
    right: int = len(s)-1
    while left < right:
        while left < right and not s[right].isalnum():
            right -= 1
        while left < right and not s[left].isalnum():
            left += 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

def isPali_copression(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(isPali("A man, a plan, a canal: Panama"))
print(isPali_copression("A man, a plan, a canal: Panama"))



# --- lets try two sum just for practice...



def two_sum_pra(arr: list[int], target: int) -> list[int]:
    """
    we solve this by two pointers patterns - Opposite.
    it's only work effeciently if the array is sorted.
    we can track down from two pointers and take it's sum and compare with target.
    """
    left: int = 0
    right: int = len(arr)-1
    while left <= right:
        total: int = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif target > total:
            left += 1
        else:
            right -= 1

    return [0, 0]




#COntainer with most water -- we will solve this letter.

def contain_most_water(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    res = 0
    while left < right:
        width = right - left
        height = min(arr[left], arr[right])
        area = width * height
        res = max(res, area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return res

print(contain_most_water([0,2]))


#THREE SUM - SORTED ARRAY.
#the three sum in sorted array means -
#any distinct elements from sorted array and it's sum shoudl be eqaul to 0.
def three_sum(arr: list[int]) -> list[int]:
    """
    so in two pointer - opposite direction pattern. 
    how should we calculate the three distinct values.
    i think we have to add the condition here. where,
    if the addition of first left+right is equal to 0 or gt(- or +) way then we right-=1 otherwise left+=1
    """
    arr.sort()
    total = 0
    res = []
    for i in range(len(arr)):
        left: int = i+1
        right: int = len(arr)-1
        while left < right:
            total = arr[i]+arr[left]+arr[right]
            if total == 0:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1

            elif total < 0:
                right -= 1
            else:
                left += 1

    return res

print(three_sum([-1, 0, 1, 2, -1, -4]))


#valid palindrom --
def valid_apli(s: str) -> bool:
    """
    we use the two pointer here - where each pointer check is it similar if yes them move inward.
    also check is is isalnum() or not if not them move inward. 
    """
    left = 0
    right = len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1


    return True

print(valid_apli("rracecar"))

