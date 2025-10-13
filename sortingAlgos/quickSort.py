from typing import List

class Solution:
    def problem(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        p = arr[-1]
        left = [x for x in arr[:-1] if x <= p]
        right = [x for x in arr[:-1] if x > p]
        return self.problem(left) + [p] + self.problem(right)


sol = Solution()
print(sol.problem([2, 3, 1]))
