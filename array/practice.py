
#TWO POINTER CLASS.
class twoPointers:
    def __init__(self, arr):
        self.arr = arr

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



