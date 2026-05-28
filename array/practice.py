
#TWO POINTER CLASS.
class twoPointers:
    def __init__(self, arr):
        self.arr = arr

    #--- OPPOSITE DIRECTION POINTERS EXAMPLES
    #two sum (sorted arr) 
    def twoSum(self, target):
        left = 0
        right = len(self.arr)-1
        while left < right:
            currSum = self.arr[left] + self.nums[right]
            if currSum == target:
                return [left+1, right+1]
            elif currSum > target:
                right -= 1
            else:
                left += 1

        return [0, 0]


    #rev a string
    def revString(self, word):
        arr = list(word)
        left = 0
        right = len(arr)-1 
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return ''.join(arr)

    # TWO POINTERS - FAST AND SLOW.
    #Batch one.....
    def remove_ele(self, val) -> list[int]:
        """
        Given : arr and val, remove the ele which are eq to val. 
        Ask: 
            1. we're using the fast-slow pointers, where fast trace the array and slow remove the element.
        Psudo:
            initialise slow eq to 0
            iterate over the array as fast.
                if fast ele is neq to val:
                    swap the slow with fast.... it will throw the similar to end.
                    increament slow by one

            return the arr with slice as [:sl]
        """
        sl = 0
        for f in range(len(self.arr)):
            if self.arr[f] != val:
                self.arr[sl], self.arr[f] = self.arr[f], self.arr[sl]
                sl += 1
        return arr[:sl]


    def move_zeros(self) -> list[int]:
        """
        Given: arr - we have to move all zeors to end.
        Ask: we use similar fast-slow pointer - they actually best for filtering the elements 
            at the end we just have to return the actual part of array which is correct!
        Psudo:
            initialize fast and slow variables. (fast at iteration value)
            iterate over the array as fast pointer.
                if fast ele neq to zero:
                    swap the non-zero element to start of the array.
                    increament the slow pointer.
            walla - you get you'r answer.
        """
        slow = 0
        fast = 0

        while fast < len(self.arr):
            if self.arr[fast] != 0:
                self.arr[fast], self.arr[slow] = self.arr[slow], self.arr[fast]
                slow += 1

                
            fast += 1

        return self.arr


    def rem_even(self) -> list[int]:
        slow: int = 0
        fast: int = 0
        while fast < len(self.arr):
            if self.arr[fast]%2!=0:
                self.arr[fast], self.arr[slow] = self.arr[slow], self.arr[fast] 
                slow += 1

            fast += 1
        return self.arr[:slow]

    def rem_char(self, c) -> str:
        slow = 0
        fast = 0
        str_is = "banana"
        chars = []
        while fast < len(str_is):
            if str_is[fast] != c:
                chars.append(str_is[fast])
                slow += 1
            fast += 1
        #new_str = "".join([char for char in str_is if char != c])
        return "".join(chars)


    #TWO POINTERS - BATCH TWO - DUBLICATES
    def rem_dubl_sorted(self) -> list[int]:
        slow = 0
        for fast in range(1, len(self.arr)):
            if self.arr[fast] != self.arr[slow]:
                slow += 1
                self.arr[slow] = self.arr[fast]

        return self.arr[:slow+1]

    def rem_dubl_two(self, k: int) -> list[int]:
        """
        Given: arr and k.
        Ask: 
            1. we have to remove the dublicates, but have to keep k's similar elements.
            2. in-place array - means no dublication needed
        Questions:
            1. we can use the fast&slow, but how to keep the k's similar elements.
            2. what condition we can pass the fast pointer to next element.
                - fast != slow: (where fast is at 1st idx, and slow at 0'th idx)
                - 
        Psudo:
            - initialize slow and hash_set
            - iterate over the array 1..n as fast
	            - if fast and slow eq and hash_set[slow] eq k_max 
	                - arr[hash_set[slow]] = arr[fast]
	                - hash_set[slow] = 0
	                - slow += 1
	            - elif arr[fast] in hash_set: 
	                - hash_set[slow] += 1
	                - slow += 1
                - else:
	                - hash_set[slow] = 1
        """

        # below code given by anthropic claude given 
#        freq = {}
#        slow = 0
#        for i in range(len(self.arr)):
#            ele = self.arr[i]
#            if freq.get(ele, 1) < k :
#                print("hey")
#                self.arr[slow] = ele
#                slow += 1
#                freq[ele] = freq.get(ele, 1)
        
        #return arr[:slow]

        #below code given by chatGPT. for sorted orrder
#        slow = 0
#        for i in range(k, len(self.arr)):
#            if self.arr[i] != self.arr[slow-k]:
#                self.arr[slow] = self.arr[i]
#                slow += 1

        #return self.arr

        slow = 0
        freq_map = {}
        arr = self.arr

        for i in range(len(arr)):
            ele = arr[i]

            if ele not in freq_map:
                freq_map[ele] = 1
                arr[slow] = ele
                slow += 1

            elif freq_map[ele] < k:
                freq_map[ele] += 1
                arr[slow] = ele
                slow += 1

        return arr[:slow]

        
    def rem_dubl_unsorted(self):
        hash_set = set()
        arr = self.arr
        slow = 0
        for i in range(len(arr)):
            ele = arr[i]
            if ele not in hash_set:
                hash_set.add(ele)
                arr[slow] = ele
                slow += 1
        
        return arr
        #-----

    def part_ev_and_odd(self):
        arr = self.arr
        slow = 0
        for i in range(len(arr)):
            if arr[i]%2==0:
                arr[slow], arr[i] = arr[i], arr[slow]
                slow += 1


        return arr, slow

    def move_neg_to_left(self):
        arr = self.arr
        slow = 0
        for i in range(len(arr)):
            if arr[i] < 0:
                arr[slow] = arr[i]
                slow += 1

            if arr[slow] > 0:
                arr[i] = arr[slow]

        return arr

arr = [1, -2, 3, -4, 5, -6]
tp = twoPointers(arr)
#ph1 = tp.remove_ele(3)
#ph1 = tp.move_zeros()
#ph1 = tp.rem_even()
#ph1 = tp.rem_char("a")
#ph2 = tp.rem_dubl_sorted()
#ph2 = tp.rem_dubl_two(2)
#ph2 = tp.rem_dubl_unsorted()
#ph3 = tp.part_ev_and_odd()
ph3 = tp.move_neg_to_left()
print(ph3)


# ----------------------------------------------------------------------
# DSA Array and Prefix Sums questions from easy to hard in total 10 questions.

class PrefixAlgo:
    def __init__(self, arr):
        self.arr = arr

    def prefix_sum(self):
        for i in range(1, len(self.arr)):
            self.arr[i] += self.arr[i-1]
        return self.arr

    def range_sum(self, l, r):
        res = 0
        for i in range(len(self.arr)):
            if i >= l and i <= r: 
                res += self.arr[i]

        return res

    def pivot_idx(self): #prefix way.
        total_sum = sum(self.arr)
        leftSum = 0
        for i in range(len(self.arr)):
            rightSum = total_sum - leftSum - self.arr[i]

            if leftSum == rightSum:
                return i

            leftSum += self.arr[i]
        
        return -1

    def pivot_idx_two(self): #sliding windows way.
        res = 0
        left, right = 0, len(self.arr)-1
        leftSum, rightSum = self.arr[left], self.arr[right]
        while left < right:
            if leftSum < rightSum:
                left += 1
                leftSum += self.arr[left]
            elif leftSum > rightSum:
                right -= 1
                rightSum += self.arr[right]
            else:
                left += 1
                right -= 1
                res = left

        return res
            
    def count_even_prefix(self, arr, choose):
        cnt = 0
        for i in range(len(arr)-1):
            if i > 0:
                arr[i-1] += arr[i+1]
            if choose == "odd" and arr[i]%2!=0:
                cnt += 1
            if choose == "even" and arr[i]%2==0:
                cnt += 1

        return cnt, arr

    def left_and_right_diff(self): #brute force apprpach..
        res = [0]*len(self.arr)
        for i in range(len(res)):
            res[i] = abs(sum(self.arr[i+1:]) - sum(self.arr[:i]))
            #print(self.arr[:i], sum(self.arr[:i]))
        return res

    def left_and_right_diff_two(self): #optimal approach.
        total_sum = sum(self.arr)
        left_sum = 0
        for i in range(len(self.arr)):
            curr = self.arr[i]
            right_sum = total_sum - left_sum - curr
            
            arr[i] = abs(right_sum - left_sum)

            left_sum += curr 

        return self.arr


arr = [10, 4, 8, 3]
pre_algo = PrefixAlgo(arr)
#pr1 = pre_algo.prefix_sum()
#pr2 = pre_algo.range_sum(1, 3)
#pr3 = pre_algo.pivot_idx()
#pr4 = pre_algo.pivot_idx_two()
#pr5 = pre_algo.count_even_prefix([1, 2, 3, 4], "odd")
#pr6 = pre_algo.left_and_right_diff()
pr7 = pre_algo.left_and_right_diff_two()
print("CODE HERE: ", pr7)






