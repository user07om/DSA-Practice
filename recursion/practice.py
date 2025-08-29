from typing import List

#print 1 to n numbers.
def num1toN(num: int):
    #base case, making input smaller
    if num==1:
        return num
    
    #hyphothesis, where you take the dicison to make the input smaller
    #just think about two step ahead of the recursion, you don't have to plan the whole
    #recurssion process till the base condition.
    num1toN(num-1)

    #induxtion - 
    print(num)

#num1toN(8)

#_--------------------------------  OCCURING ERROR
def sortRec(arr: List[int]): 
    if len(arr) <= 0:
        return arr

    if arr[-1] < sortRec(arr[:1]):
        arr.append(arr[-1])
    print(arr)

#sortRec([3, 2, 1])



#--------------------------------
def getMaxEle(arr: list) -> int:
    """
    HOW THIS CODE WORK:
    1. base case - you know what it is - if cirtain condition match return the first element.
    2. hypotheses, where we use the recursion process to do some  logic to create the recursin
        tree.
        * 2, 5, 1, 6 -> here the first element/index will use for comparision.
        so the process would look like this, at first call the first index is 2
        at second call the first index is 5 and so on until it reaches length of 1 then
        in recursive tree order. 6 will return then 1, 6 then 5,1,6.
    """

    #base case 
    if len(arr) == 1:
        return arr[0]

    #recursion step - hypothesis.
    max_ele = getMaxEle(arr[1:])

    #induxtion.
    if arr[0] > max_ele:
        return arr[0]
    else:
        return max_ele


print(getMaxEle([3, 1 ,4, 5, 9]))


#---------------------------------------------
# reverse a string
def rev_str(s: str):
    if len(s) <= 1:
        return s

    return rev_str(s[1:]) + s[0]

print(rev_str("omkar"))


#------------------------------
# sort the list.
def sort_arr(nums):
    """ THOUGH PROCESS.
    1. base case - if there's only one element it's already sorted.
    2. hypothesis - assume sort_arr(nums[1:]) gives me sorted array.
    3. induxtion - now i just need to place the nums[0] if the correct place in sorted arr dummy
        1. if it belong in front put it there.
        2. otherwise keep inserting the first element of dummy and recursively inserting into the rest.
    """
    res = []

    #base case.
    if len(nums) == 1:
        return nums

    dummy = sort_arr(nums[1:])
    if nums[0] <= dummy[0]:
        res = [nums[0]]+dummy
    else:
        res = [dummy[0]] + sort_arr([nums[0]]+dummy[1:])

    return res


print(sort_arr([3, 4, 2, 1]))


#-----------------------------------
#sum of list.

def sum_list(arr):
    if len(arr) <= 1:
        return arr[0]

    return arr[0] + sum_list(arr[1:])

print(sum_list([3, 1, 2]))


#--------------------------
#cheeck if palindrome is palindrome

def is_pali(s):
    if len(s) == 1:
        return True

    return s[0] == s[-1] and is_pali(s[1:-1])

print(is_pali("Hello"))


#-----------------------------------
#count occurences of the element.

def count_x(arr, x):
    if not arr:
        return 0

    smaller = count_x(arr[1:], x)
    return (1 if arr[0] == x else 0) + smaller

print(count_x([3, 1, 4, 2, 3, 2, 4, 3, 3], 2))


#------------------------------
#small element in the arr

def small_ele(arr):
    if len(arr) <= 1:
        return arr[0]

    small = small_ele(arr[1:])
    if arr[0] < small:
        return arr[0]
    else:
        return small

print(small_ele([2, 1, 4]))



#-----------------------------
#factorial 

def facto(n):
    if n==0:
        return 1

    return n*facto(n-1)

print(facto(3))


#--------------------------------
#




