# lets try the bubble sort algo -
def bubble_sort(arr):
    """
    what we actually do here.
    1. we usually use the two iteration
    2. outer loop will iterate over the arr except the last one.
    3. inner loop will iterate over the arr - which starts from outer loop i+1 because we need the second element and i is the first index
        till length of arr till the last index of array
    4. in the inner loop we define the logic of swapping algo - its an pythonic way.
    5. at the end we return the array.
    """
    n = len(arr)   #3
    for i in range(n-1):  #till 2
        for j in range(i+1, n):  #for the first iteration - 
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr


def quick_sort(arr):
    """
    what is the quick sort algo -
    1. it recursively call the same function as left and right
    2. the base case of this function is, if len or arr < 1 return arr.
    3. it takes any index from the element, propably the last index. and compare it to each element of the array.
    4. recursion: 
        - in the return statement we return the quick_sort(left) + [mid] + quick_sort(right).
        - so the first quick_sort function takes the left side of the array, with corresponding first element as the pivot element
        - and the second quick_sort function takes the right side of the array, with corresponding last element as the pivot element
        - so left has the [1, 1] so when does it stop? but the pivot element is 1 right?
    """
    left = []
    mid = []
    right = []
    if len(arr) <= 1:    #its an edge case which will stop the loop/recursive-call.
        print(left, mid, right)
        return arr
    
    piv = arr[-1]

    #with compression.
    #left = [x for x in arr if x < mid]   #why arr[x] < mid : because left side containes the lesser values 
    #right = [x for x in arr if x > mid]   #and right side containes bigger vlaues.

    #without compression.
    for i in arr:
        if i < piv:
            left.append(i)
        elif i > piv:
            right.append(i)
        else:
            mid.append(i)

    print(left, mid, right)

    return quick_sort(left)+mid+quick_sort(right)



#print(bubble_sort([3, 1, 2]))
#print(quick_sort([3, 1, 4, 2]))

def sum_digit(n: int) -> int:
    if n < 10:
        return n

    return n%10 + sum_digit(n//10) #call-stack[12345, 1234, 123, 12, 1]

# print(sum_digit(9604094454))


def rev_str(s: str) -> str:
    if s <= 1:
        return s

    return s[-1] + rev_str(s[:-1])

#like we have to think in reverse for recursive algos. lets try another one example.

#palindrom check recursively.
def pali_check(s: str) -> bool:
    if len(s) <= 1:
        print(s)
        return True
    return s[1] == s[-1] and pali_check(s[1:-1])
    
name = "omkar"
print(name[1:-1])
print(pali_check(name))