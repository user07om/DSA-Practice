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

#_--------------------------------

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
