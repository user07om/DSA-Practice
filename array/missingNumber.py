
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # FIRST APPRAOCH
        # missing = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] != missing and i < len(nums):
        #         missing = i
        #     elif i > len(nums):
        #         missing = i+1
        #     i += 1

        #GPT APPROACH
        # expected_sum = len(nums) * (len(nums)+1)//2
        # real_sum = sum(nums)
        # return expected_sum - real_sum

        #XOR APPROACH
        n = len(nums)
        ans = n
        for i in range(n):
            ans ^= i ^ nums[i]
        return ans


sol = Solution()
print(sol.missingNumber([3, 0, 1]))
