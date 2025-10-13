from typing import List

class Solution:
    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr)<=1:
            return arr

        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        res.extend(left[i:])
        res.extend(right[j:])

        return res


sol = Solution()
print(sol.merge_sort([3, 2, 1]))
