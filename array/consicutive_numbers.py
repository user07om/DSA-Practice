from typing import List

class Solution:
    #my appraoch - trying to implement and structure the problem
    def my_approch(self, arr: List[int]) -> int:
        """
        Given: arr of int. 
        Output: int - lenght of output array
        Task/Logic:
            1. the longest consecutive seqence mean.s
                - the num which are greater then previous one.
                - not required to be in order.
                - dublicate ignored.
                - the output array should be in sequntial order.
            2. we'll just do the max element.
                - find the smallest one, then compare each element
                    with that and if condition match 
                    we'll append it to the res array.
        """
        if not arr: return 0   # if no arr return 0
        s_arr = sorted(set(arr))  #removed the dublicates and sorted the arr
        
        #find the minimul value.
        min_v = s_arr[0]
        count = 0
        res = []

        for i in range(len(s_arr)):
            if s_arr[i] < min_v:
                min_v = s_arr[i]

        #res.append(min_v)

        current = min_v
        while count <= len(s_arr): 
            if current in s_arr:
                res.append(current)
            count+=1
            current+=1

        print(res)
        return len(res)


    #initail appraoch - improvements has been made, little one only... 
    def first_approach(self, arr):
        if not arr: return 0
        s_arr = sorted(set(arr))

        m_val = 1
        c_val = 1

        for i in range(1, len(s_arr)):
            if s_arr[i] == s_arr[i-1]+1:
                c_val += 1
            else:
                m_val = max(m_val, c_val)
                c_val = 1

        return max(m_val, c_val)


    def sec_approach(self, arr):
        if not arr: return 0

        hashSet = set(arr)
        curr_v = 0
        max_v = 0

        for n in hashSet:
            if n-1 not in hashSet:
                curr_v = 0

                while n in hashSet:
                    n += 1
                    curr_v += 1
            
                max_v = max(max_v, curr_v) 

        return max_v


            



nums=[9,1,4,7,3,-1,0,5,8,-1,6]

#solution here.
sol = Solution()
print(sol.my_approch(nums))
print(sol.first_approach(nums))
print(sol.sec_approach(nums))
