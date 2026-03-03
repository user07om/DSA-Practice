from collections import Counter
from itertools import accumulate
import heapq

class HashSet:
    def __init__(self, arr):
        self.arr = arr

    def count_freq(self):
        freq = {}
        for x in self.arr:
            freq[x] = freq.get(x, 0)+1

        return freq

    def maj_ele(self):
        freq = {}
        for x in self.arr:
            if freq.get(x) and freq.get(x) >= len(self.arr)//2:
                return x
            freq[x] = freq.get(x, 0)+1

        return nums[0]

    def top_k_freq(self, j):
        freq = {} #simpler version would be Counter(nums)
        for x in self.arr:
            freq[x] = freq.get(x, 0)+1

        heap = []
        for k, v in freq.items():
            heapq.heappush(heap, (v, k))
            if len(heap) > j:
                heapq.heappop(heap)

        return [x for fre, x in heap]

    def all_dubli(self):
        freq = {}
        res = []
        for x in self.arr:
            if freq.get(x):
                res.append(x)
            freq[x] = freq.get(x, 0)+1

        print("yeah---", freq)
        return res


    def counter_show(self):
        counter = Counter(self.arr)
        return counter

    def freqSort(self):
        s = list(self.arr)
        freq = Counter(s)
        return "".join(sorted(s, key=lambda x: -freq[x]))

    def uni_occur(self):
        freq = Counter(self.arr)
        return len(freq.values()) == len(set(freq.values())) 

    def degree_arr_sucks(self):
        """
        This code works fine, but couldn't resolve the one usecase when where if the all keys freq is same
        or atleast 2 keys freq is same then it chooses the bigger number even though the smaller number has
        the less width then bigger number.
        """
        freq = Counter(self.arr)
        max_v = float("-inf")
        degree_ele = float("-inf")
        degree_ele_arr = []
        for key, value in freq.items():
            if value > max_v or (value == max_v and key > degree_ele):
                max_v = value
                degree_ele = key
                degree_ele_arr.append(key)

        left = 0
        right = len(self.arr)-1
        min_width = 0
        print(f"degree val: {degree_ele}, max freqence:  {max_v}")
        while left < right:
            while left < right and self.arr[left] != degree_ele:
                left += 1

            while left < right and self.arr[right] != degree_ele:
                right -= 1

            min_width = (right- left) + 1 
            break

        return min_width

    def degree_arr(self):
        first = {}
        last = {}
        freq = {}

        for i in range(len(self.arr)):
            if self.arr[i] not in first:
                first[self.arr[i]] = i

            last[self.arr[i]] = i
            freq[self.arr[i]] = freq.get(self.arr[i], 0)+1

        degree = max(freq.values())
        min_len = float("inf")

        for num in freq:
            if freq[num] == degree:
                width = (last[num] - first[num]) + 1
                min_len = min(min_len, width)

        print(first, last, freq)
        return min_len







arr = [6,5, 5, 5, 6, 6]
hs = HashSet(arr)
#pr0 = hs.all_dubli()
#pr1 = hs.maj_ele()
#pr2 = hs.top_k_freq(2)
#pr3 = hs.freqSort()
#pr4 = hs.uni_occur()
pr5 = hs.degree_arr()
#print("heap class methods ---- \n",heapq.__all__)
#print(pr3)
#print("uniqu occurences: ", pr4)
print("degree of array: ", pr5)



#insertion sort algorithm - it's just enhanced version of bubble sort.
def insertion_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        if j >= 0 and arr[j] > key:
            arr[j+1] = arr[j] 
            j -= 1

        arr[j+1] = key

    return arr

print(insertion_sort([2, 0, 1, 3]))
""" LOGIC WORKFLOW.................
FIRST ITERTAION FLOW...
i = 1, j = i-1[0]    -------variable.
key = arr[i] .....(0)
condition is .. if j ge 0 and arr[j] means(0'th index element) gt key means(1'st index element):
    0 ge 0 and 2 > 0... condtion True...
        [at fisrt pos assign 0th value] ... 1st pos = 2
        decrement the j by 1. .. so j becomes -1

    [at 0th pos assign i'th value] ... 0'th pos = 0 key value.

arr is at first iteration. [0, 2, 1, 3]

---

SECOND ITERATION FLOW...
i = 2, j = i-1[1]   -------------vairable
key = arr[i] .......(1)
condition is .. if j ge 0 and arr[j] means (1'st idx ele) gt key means (2'nd idx ele):
    1 is ge 0 and 2 > 1 ... conditiokn true...
        [at second pos assign first value] .. 2nd pos = 1
        decreament j by 1. .. so j becomes 0

    [at 1st pos i'th value] ... 1'th pos = 1 key value

arr is at second iteration. [0, 1, 2, 3]
"""


#_-----------------------------

class Hash_Frequency:
    def __init__(self, arr):
        self.arr = arr

    #EASY ONES 1-7 problems...
    def freq_count(self):
        freq = {}
        for x in self.arr:
            freq[x] = freq.get(x, 0)+1

        return freq
        #we can also use the Counter method from collections module for Frequency
        #freq = Counter(self.arr) #this will provide the object of freq.

    def first_non_char(self):
        s = list(self.arr)
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0)+1

        first_non_char = ""
        for c in s:
            if c in freq and freq.get(c) == 1:
                first_non_char = c
                break

        return first_non_char

    def most_freq_n(self) -> list[int]:
        freq = {}
        res = 0
        max_n = float("-inf")
        for x in self.arr:
            if freq.get(x) and freq[x] > max_n: 
                res = x
            freq[x] = freq.get(x, 0)+1

        return res
        
    def is_anagram_one(self, str2):
        freq = {}

        for c in self.arr:
            freq[c] = freq.get(c, 0)+1

        for c in s2:
            if c not in freq and freq[c] == 0:
                return False

            freq[c] -= 1

        return True

    def is_anagram_two(self, str2):
        s1 = Counter(self.arr)
        s2 = Counter(str2)
        if s1 == s2: 
            return True 
        else: return False

    def count_distinct(self):
        freq = {}
        count = 0
        for x in self.arr:
            freq[x] = freq.get(x, 0)+1
    
        for value in freq.values():
            if value == 1: count += 1
    
        return count 

    def maj_ele(self):
        freq = Counter(self.arr)
        for x in self.arr:
            if freq[x] and freq[x] >= len(self.arr):
                return x

        return self.arr[0]

    # medium ones
    def freq_k_one(self, k):
        freq = Counter(self.arr)
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]

    def freq_k_two(self, k):
        freq = {}
        for x in self.arr:
            freq[x] = freq.get(x, 0)+1


class Hash_Set:
    def __init__(self, arr):
        self.arr = arr

    def contains_dubli(self):
        seen = set()
        for x in self.arr:
            if x in seen:
                return True
            seen.add(x)

        return False

    def happy_numbers(self):
        seen = set()
            
        n = self.arr

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)

            total = 0
            while n > 0:
                digit = n%10
                total += digit * digit
                n //= 10    

            n = total 

        return True

    def max_cons_numb(self):
        self.arr.sort()
        seen = set(self.arr)
        max_count = float("-inf")
        for x in seen:
            if x-1 not in seen:
                curr_x = x
                count = 1

                while curr_x+1 in seen:
                    curr_x += 1
                    count += 1

                max_count = max(max_count, count)

        return max_count

class CompLookup:
    def __init__(self, arr):
        self.arr = arr

    def two_sum(self, val):
        freq = {}
        for i in range(len(self.arr)):
            target = self.arr[i] - val
            if target in freq:
                return [freq[target], i]
            freq[self.arr[i]] = i

        return [0, 0]

    def CountDiff(self, k):
        freq = {}
        count = 0
        for x in self.arr:
            print("fuck it... ", freq.get(x, 0))
            count += freq.get(x-k, 0)
            count += freq.get(x+k, 0)
            #if freq.get(x-k) or freq.get(x+k):
                #count += 1

            freq[x] = freq.get(x, 0)+1

        print(freq)
        return count

    def CountDiff_second_appr(self, k):
        count = 0
        ca = [0]*101

        for i in range(len(self.arr)):
            ca[self.arr[i]] += 1

        for i in range(len(ca)-k):
            count += ca[i] * ca[i+k]
            #print(count, ca[i], ca[i-k])

        #print(ca)
        return count

    def subarr_sum_eq_k(self, k):
        pref = 0
        count = 0
        freq = {0: 1} #default set.

        for x in self.arr:
            pref += x

            if pref - k in freq:
                count += freq[pref-k]

            freq[pref] = freq.get(pref, 0) + 1

        return count


# Frequency programs....
arr = [1, 2, 1, 2, 1, 3, 1, 3]
#arr = "silent"
#st2 = "listen"
hp_freq = Hash_Frequency(arr)
#p1 = hp_freq.maj_ele()
#p2 = hp_freq.first_non_char()
#p3 = hp_freq.most_freq_n()
#p4 = hp_freq.is_anagram_one(st2)
#p5 = hp_freq.count_distinct()
p6 = hp_freq.freq_k(2)
print("Yoo freq most_freq", p6)

# Set Programs.....
arr = [100, 4, 200, 3, 1, 2]
hp_set = Hash_Set(arr)
#p1 = hp_set.happy_numbers()
#p2 = hp_set.max_cons_numb()
#print("Yoo Set", p2)

arr = [1, 2, 2, 1]
hp_compli = CompLookup(arr)
#p1 = hp_compli.two_sum(3)
#p2 = hp_compli.CountDiff(1)
p3 = hp_compli.CountDiff_second_appr(1)
print("yooo baby: ", p3)


def SingleDig(n): #pythonic way?
    return [int(d) for d in str(n)]

def MathDig(n): #algorithmic - maths use.
    res = []
    while n > 0:
        #n %= 10
        res.insert(0, n%10)
        n //= 10

    return res

print(SingleDig(19))
print(MathDig(19))


