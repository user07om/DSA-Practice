
class InsertVal:
    """
        insert at position: there are many variations:
        - insert elemet at verious position
        - insert at beginning
        - insert at end
    """
    def __init__(self, arr):
        self.arr = arr

    def reverse_way(self, idx, val):
        self.arr.append(0) #for making the space in arr
        n = len(self.arr)
        for i in range(n-1, idx, -1):
            self.arr[i] = self.arr[i-1]

        self.arr[idx] = val

        return self.arr

    def variable_way(self, idx, val):
        self.arr.append(0) 
        n = len(self.arr)
        temp = val
        for i in range(idx, n):
            curr_ele = self.arr[i]
            self.arr[i] = temp
            temp = curr_ele

        return self.arr

    def extra_space_way(self, idx, val):
        n = len(self.arr)
        temp = [0]*(n+1)
        for i in range(len(temp)):
            if i < idx:
                temp[i] = self.arr[i]
            elif i == idx:
                temp[i] = val
            else:
                temp[i] = self.arr[i-1]

        return temp

InsertPos = InsertVal([1, 2, 3, 4, 5])
#opr_one = InsertPos.reverse_way(2, 9)
#opr_two = InsertPos.variable_way(2, 9)
opr_three = InsertPos.extra_space_way(2, 9)
print(opr_three, " operations----------------------------------------------> ")



class DeleteVal:
    """
        - delete first element 
        - delete at index
        - delete by value
    """

    def __init__(self, arr):
        self.arr = arr

    def del_first(self):
        n = len(self.arr)
        for i in range(1, n):
            self.arr[i-1] = self.arr[i]

        self.arr.pop()
        
        return self.arr

    def del_at_idx(self, idx):
        n = len(self.arr)
        #for i in range(idx, n-1):
            #self.arr[i] = self.arr[i+1]

        for i in range(idx+1, n):
            self.arr[i-1] = self.arr[i]
        self.arr.pop()

        return self.arr

    def del_val(self, val):
        n = len(self.arr)
        key = 0
        for i in range(n):
            if self.arr[i] == val:
                key = i

        for i in range(key, n-1):
            self.arr[i] = self.arr[i+1]

        self.arr.pop()

        return self.arr


delVal = DeleteVal([1,2,3,4,5])
#first = delVal.del_first()
#second = delVal.del_at_idx(2)
third = delVal.del_val(4)
print(third, " -----------------------------------> omkar here i'm")





class PartitionProblems:
    """in the partition problem the zero pattern is also there but it's okay! we're not adding in this class"""
    def __init__(self, arr):
        self.arr = arr
        self.n = len(self.arr)

    def brute_force(self): #this is not working!
        n = len(self.arr)
        cnt = 0
        for i in range(n):
            if self.arr[i] == 0:
                cnt += 1

                for j in range(n-1, n-i-1, -1):
                    self.arr[j] = self.arr[j-1]


        for _ in range(cnt):
            self.arr.pop()

        for _ in range(cnt):
            self.arr.append(0)

        return self.arr

    def rotate_zero(self):
        self.arr.sort()
        n = len(self.arr)
        zeros = self.arr.count(0)

        def rev_arr(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            return arr

        #rev_arr(self.arr, 0, zeros)
        rev_arr(self.arr, zeros, n-1)
        rev_arr(self.arr, 0, n-1)

        return self.arr

    def optimal_one(self):
        n = len(self.arr)
        slow = 0
        for fast in range(n):
            if self.arr[fast] != 0:
                self.arr[fast], self.arr[slow] = self.arr[slow], self.arr[fast]
                slow += 1

        return self.arr

    def optimal_two(self):
        n = len(self.arr)
        slow = 0
        for fast in range(n):
            if self.arr[fast] != 0:
                self.arr[slow] = self.arr[fast]
                slow += 1

        for i in range(slow, n):
            self.arr[i] = 0
            
        return self.arr

    def rem_element(self, k): #same fast and slow pointer approach! if it's not equal to k then swap with fast and slow+=1.
        s = 0
        for i in range(self.n):
            if self.arr[i] != k:
                self.arr[s] = self.arr[i]
                s += 1

        return self.arr[:s]
            
    def rem_dublicates(self): #using fast and slow pointer, the past ele at slow pointer are correct and other needs correction.
        s = 0
        for i in range(self.n):
            if self.arr[i] != self.arr[s]:
                s += 1
                self.arr[s] = self.arr[i]

        return self.arr[:s+1]

    #bruteforce approach to move negetive to left.
    def negative_partition(self): #it has some issues, cannot solve this right now?
        s = 0
        for i in range(self.n):
            if self.arr[i] < 0:
                self.arr[s] = self.arr[i]
                s += 1

        if not self.isSap():
            self.negative_partition()

        return self.arr

    def isSap(self):
        count = 0
        for i in range(self.n-1):
            if self.arr[i] >= 0 and self.arr[i+1] < 0:
                count += 1

        print(count)
        return count == 1

    def mvNeg_slow_fast(self): #read the array using fast and do the modification using slow pointer.
        s = 0
        for i in range(len(self.arr)):
            if self.arr[i] >= 0:
                self.arr[i], self.arr[s] = self.arr[s], self.arr[i]
                s += 1

        return self.arr

    def mvNeg_opposite_pointer(self): #we change the l or r pointer by chekcing it's negative or not and then we swap it.
        l = 0
        r = len(self.arr)-1
        while l < r:
            if self.arr[l] >= 0:
                l += 1
            elif self.arr[r] < 0:
                r -= 1
            else:
                self.arr[l], self.arr[r] = self.arr[r], self.arr[l]
                l += 1
                r -= 1

        return self.arr


#PartProblem = PartitionProblems([1, 1, 2, 2, 3, 3]) 
PartProblem = PartitionProblems([1, 0, 0, 1, 2, 0]) 
#PartProblem = PartitionProblems([1, -2, 3, -4, 5, 1, 5, -2]) 
#first = PartProblem.rem_element(3)
#second = PartProblem.rem_dublicates()
#third = PartProblem.negative_partition()
#forth = PartProblem.mvNeg_slow_fast()
fifth = PartProblem.mvNeg_opposite_pointer()
print(fifth, "yo how are you!")


#opr = PartProblem.optimal_two()
opr = PartProblem.optimal_one()
#opr = PartProblem.rotate_zero()
#opr = PartProblem.brute_force() # it has some issues, need to check and correct it!
print(opr, "move zeros as optimal approach")




class QueryIT:
    def __init__(self, arr):
        self.arr = arr

    def second_largest(self):
        largest = float("-inf")
        ans = largest

        for x in self.arr:
            if largest > x > ans:
                ans = x
            elif x > largest:
                ans = largest
                largest = x

        return ans
    
    #kth means the first, second or third.. etc. we gonna try different approaches. then we'll move to optimal one.
    def kth_bruteforce(self, k):
        n = len(self.arr)
        self.arr.sort()
        return self.arr[n-k]
        
    def quick_select_kth(self, k):

        def partit(self, arr, left, right):
            idx = left-1; pivot = arr[right]
            for x in arr:
                if x <= pivot:
                    idx += 1
                    x, arr[idx] = arr[idx], x

            idx += 1
            arr[idx], pivot = pivot, arr[idx]

            return idx

        def quick_select(self, arr, left, right):
            if left < right:
                p_idx = partit(arr, left, right)
                quick_select(arr, left, p_idx-1)
                quick_select(arr, p_idx+1, right)

            return 



def partition(arr: list[int], left: int, right: int) -> int:
    idx = left-1; pivot = arr[right] 
    for i in range(left, right):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    idx += 1
    print(idx)
    arr[right], arr[idx] = arr[idx], arr[right]

    return idx

def quick_sort(arr, left, right):
    if left <= right:
        p_idx = partition(arr, left, right) #get the idx 
        quick_sort(arr, left, p_idx-1)
        quick_sort(arr, p_idx+1, right)

    return arr

    
arr = [3,1,2,4]
print(quick_sort(arr, 0, len(arr)-1), "fucking fuck the fucker.....")


query_it = QueryIT([1, 129, 2, 75, 92, 3, 1, 7])
#opr = query_it.second_largest()
opr = query_it.kth_bruteforce(2)
print(opr, " -----------------------------  the kth largest value!")



















def secLarge(arr):
    large = arr[0]
    sec_large = large
    for x in arr:
        if large > x > sec_large:
            sec_large = x
        elif x > large:
            sec_large = large
            large = x

    return large, sec_large

print(secLarge([1, 2, 3, 4]))

arr = [4, 9, 1, 5, 6, 8]; k=3
def kthLargest(arr, k):
    for _ in range(k-1):
        max_v = arr[0]
        key = 0
        for i in range(len(arr)):
            if arr[i] > max_v:
                max_v = arr[i]
                key = i
        
        arr.pop(key)


    return max(arr)


print(kthLargest(arr, k), "kth largest")


def countFreq(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0)+1

    return freq

def cFreqTwo(arr):
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    return freq

print(cFreqTwo([1, 1, 2, 2, 3, 3, 3, 4]))

def isSorted(arr):
    sort_flag = True
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            sort_flag = False

    return sort_flag

print(isSorted([1, 3, 5, 4]))

#def mergeArr(arr1, arr2):
    #i = 0
    #j = 0


#num1 = [1, 2, 3]; num2 = [1, 2, 3, 4, 5]
#if len(num1) > len(num2): n = len(num1)
#else: n = len(num2)
#print(n)


#arr = [1, 2, 3, 4] # Output: [1, 3, 6, 10]
#res = []
#for i in range(len(arr)+1):
    #res.append(sum(arr[:i]))
#print(res)

arr = [1, 2, 3, 4] # Output: [1, 3, 6, 10]
inputArr = [1, 2, 3, 4]
def prefSum(arr):
    arr.append(0)
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = 0

    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]

    return arr

def rangeSum(pre, left, right):
    rightSum = pre[right]
    leftSum = pre[left] if left > 0 else 0
    return rightSum - leftSum

def targetSum(arr, target):
    left = 0
    right = len(arr)-1
    ans = []
    while left < right:
        total = arr[right] - arr[left]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            ans = inputArr[left:right]
            left += 1
            right -= 1


    return ans

prefSum(arr)
print(arr, inputArr)
print(rangeSum(arr, -1, 2))
print(targetSum(arr, 6))


arr = [5, 4, -1, 7, 8]
#arr = [1, 2, 3, 4, 5]
max_v = float("-inf")
for i in range(len(arr)):
    for j in range(i, len(arr)+1):
        for k in range(i, j):
            #res.append(sum(arr[i:j]))
            print(arr[k], end=" ")
        print(" -- ", sum(arr[i:j]))
        if sum(arr[i:j]) > max_v:
            max_v = sum(arr[i:j])
    print()


print(max_v, "---------------------------------------------------")


def equiIdx(arr):
    ans = -1
    for i in range(1, len(arr)-1):
        is_valid = sum(arr[:i]) == sum(arr[i+1:])
        if is_valid:
            ans = i
            break

    return arr[ans]

print(equiIdx([3, 1, 5, 2, 2]))
arr = [3, 1, 5, 2, 2]
def equilibreumIdx(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] + arr[i]


equilibreumIdx(arr)
print(arr)
    


def validPali(s):
    s = s.lower()
    l = 0
    r = len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1

        while l < r and not s[r].isalnum():
            r -= 1

        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True


print(validPali("A man, a plan, a canal: Panama"))


arr = [-4,-1,0,3,10] 
res = []
def SquarSort(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        if abs(arr[left]**2) > abs(arr[right]**2):
            res.append(abs(arr[left]**2))
            left += 1
        else:
            res.append(abs(arr[right]**2))
            right -= 1

    return res

print(SquarSort(arr))


arr = [1, 1, 1, 2, 2, 3, 3]
def remDubliCates(arr):
    slow = 2
    for fast in range(2, len(arr)):
        if arr[fast] != arr[slow-2]:
            arr[slow] = arr[fast]
            slow +=1

    return arr[:slow]
print(remDubliCates(arr))

res = []
def remDubliBrute(arr): #bruteforce approach:
    res.append(arr[0])
    res.append(arr[1])

    prev = 1
    for read in range(2, len(arr)):
        while arr[read] != arr[prev]:
            res.append(read)
            prev = read 
        
        continue


    return res
print(remDubliBrute(arr), "something is wrong!")

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
