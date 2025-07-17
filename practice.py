def find_max(arr: list) -> int:
    """
    1. break down into steps (decomposition)
    2. start with assumption (pattern recognition) 
    """
    max_val = arr[0] #assume first number is larget
    for i in range(len(arr)):
        # question your self, is my current assumption still valid
        if arr[i] > max_val:
            max_val = arr[i] #udpate/fix asuption if wrong.
    
    return max_val

#print(find_max([3, 1, 33]))


def find_rep(arr: list) -> None:
    count: int = 1 

    current: int = arr[0]
    ele_is: int = 0
    for i in range(len(arr)-1):
        if arr[i] == current:
            count += 1
        else:
            print(f"the count of {current} is {count}")
            current = arr[i]
            count = 1


#find_rep([3, 2, 3, 9, 5, 4, 4, 4, 4])


def sort_algo(arr: list) -> list:
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    
    return arr

def bin_search(arr: list, t: int) -> list:
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == t:
            return mid
        if arr[mid] < t:
            left = mid+1
        else:
            right = mid-1
    return -1


#pattern recogination training.
def analyze_seq(arr: list) -> None:
    #pattern 1: running sum
    sum_up = 0
    for i in range(len(arr)):
        sum_up += arr[i]
    print(f"sum-up of arr elements is {sum_up}")

    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1] 
        diff = arr[i] - arr[i-1]
        print(f"difference between two elements {diff}")

    base = arr[0]
    for i in range(len(arr)):
        if arr[i] % base == 0:
            print(f"{arr[i]} is multiple of {base}")
    

def list_dubli(arr: list) -> list: #---------------need to fix, what could be the issue is.
    result = []
    for i in range(len(arr)): #this outer loop 
        for j in range(i+1, len(arr)): #inner loop for 
            if arr[i] == arr[j]:
                result.append(arr[j])
    return result

print(list_dubli([3, 3, 1, 2, 2, 8, 8]))


#two sum problem, return the pairs of indices.

def two_sum(arr: list, t: int) -> list:
    seen = set()
    result = []
    for num in arr:
        needed = t - num;
        if needed in seen:
            result.append([num, needed])
        seen.add(num)
    
#     return result
def two_sum_diff_apr(arr: list, t: int) -> list:
    result = [] #contain the list of indices
    seen = set()
    for i in range(len(arr)):
        compliment = t - arr[i]


print(two_sum([3, 2, 4, 5, 7, 2], 9))


#-------------------------------------------------------
#two pointers and sliding window practice.
#problem one - check if sum of target is present in the array.
def two_sum_target(arr, target):
    left, right = 0, len(arr)-1
    while left<right:
        current_sum = arr[left]+arr[right]
        if current_sum == target:
            return True 
        elif current_sum < target:
            left+=1
        else:
            right-=1 
    return False


#brute force approach --
def twoSum_bforch(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]==target:
                return True
    
    return False
#example
print("here we are", twoSum_bforch([1, 2, 3, 4, 5], 932))



#dublicated from the array
def count_distinct_value(arr):
    if len(arr)<=1:
        return -1
    
    write_i = 1
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            arr[write_i] = arr[i]
            write_i += 1
    return write_i

print(count_distinct_value([1, 1, 2]))
        

