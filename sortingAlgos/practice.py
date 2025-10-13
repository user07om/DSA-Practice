from typing import List

class Solution:

    # MERGE SORT ALGORITHM
    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1

        res.extend(left[i:])
        res.extend(right[j:])

        return res

    # INSERTION SORT.
    def insertionSort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key

        return arr

    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        p = arr[-1]
        left = self.quick_sort([x for x in arr if x < p])
        right = self.quick_sort([x for x in arr if x > p])
        return self.quick_sort(left)+[p]+self.quick_sort(right)

                


sol = Solution()
print(sol.merge_sort([3, 2, 1]))
print(sol.insertionSort([3, 2, 1]))
print(sol.quick_sort([3, 2, 5, 1]))

