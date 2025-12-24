from typing import List

class Solution:
    def my_approach(self, arr: List) -> List[int]:
        res = []
        for i in range(len(arr)):
            val = 1
            for j in range(len(arr)):
                if i == j: continue
                val *= nums[j]
            
            res.append(val)

        return res


    def first_appraoch(self, arr: List[int]) -> List[int]:
        ...


nums = [1, 2, 4, 6]
sol = Solution()
print(sol.my_approach(nums))
