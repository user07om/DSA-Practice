class ContainsDublicatesII:
    def getDubli(nums: list, k: int) -> bool:
        seen: set = set()  #set the distince container as Set()
        i: int = 0  #set the inital value.
        j: int = 0
        while j < len(nums):  #iterate over the nums range.
            if nums[j] in seen:  # check is index value exist in seen or not., if yes then return true.
                return True

            seen.add(nums[j])  # add the values in the seen.

            if j-i>=k:  # here condition for checking is j-i not cross the k'th value. if then 
                seen.remove(nums[i])  # remove the i'th index from seen
                i+=1  # and increament the i'th index. for keep the window constant.
            j+=1  # we're using the while loop so need to increament the j, else we can use the for loop.

        return False
    
""" THE HASHMAP WEY
hashmap = {}
for i in range(len(arr)):
    if arr[i] in hashmap and hashmap[arr[i]]-i<=k:
        return True
    hashmap[arr[i]] = i
return False
"""


nums = [1, 2, 3, 1]
contDubli = ContainsDublicatesII
print(contDubli.getDubli(nums, 3))
