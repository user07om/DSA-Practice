
def lr_arr_op(arr: list) -> list:
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

print(lr_arr_op([1,2,3,4,5]))


class Solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def rotate_arr(self):
        #modulo of k, if we keep as k as it is, it will throw an error "index out or range"
        k = self.k%len(self.nums)
        self.reverse_arr(self.nums, 0, len(self.nums)-1)
        self.reverse_arr(self.nums, 0, self.k-1)
        return self.reverse_arr(self.nums, self.k, len(self.nums)-1)


    #using this function for recurstion call
    def reverse_arr(self, nums, start, end):
        while start < end:
            # swap elements
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        return nums


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
problem = Solution(arr, k)
print(problem.rotate_arr())

