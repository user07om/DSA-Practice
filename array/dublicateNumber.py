class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                return nums[i]
            seen[nums[i]] = i
            i+=1
        
        return -1
