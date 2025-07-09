#simple binary search algo practice.

def three_sum(arr, target):
    """
    1. three sum problem psudo code
        - sort the array in O(n) time
        - then iterate over the loop and check for the target and if target not found then assign the result to the array and return the result
        - if target found then iterate over the loop and check for the target and if target not found then assign the result to the array and return the result
    """
    # bruteforce code - O(n*3) time
    result = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    result.append([arr[i], arr[j], arr[k]])

    # effecient code - O(n) time
    arr.sort()
    result = []
    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left, right = i+1, len(arr)-1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1
    return result

print(three_sum([2, 1, 5, 3], 6))
"""
class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) <= 1:
            return 1 if nums[0] < target else 0
        left, right = 0, len(nums)-1
        result = 0

        
        while (left<right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                result = left+1
            else:
                right = mid - 1
                result = right+1 if target >= nums[0] else right

        return result+1 if result==-1 else result
"""