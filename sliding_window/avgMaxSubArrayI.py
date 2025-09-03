class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # i, j = 0, 0
        # max_avg = 0
        # curr_sum = 0
        # dummyRes = []
        # res = set()
        # while j < len(nums):
        
        #     if len(nums)<=1:
        #         return nums[0]

        #     curr_sum += nums[j]
            
        #     if j-i+1==k:
        #         max_avg = max(max_avg, (curr_sum/k))
        #         curr_sum -= nums[i]
        #         i+=1
        #         j+=1
        #     else:
        #         j+=1
        # return max_avg

        size = len(nums)
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        max_avg = curr_sum / k

        for i in range(k, size):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]
            avg = curr_sum / k
            max_avg = max(max_avg, avg)

        return max_avg