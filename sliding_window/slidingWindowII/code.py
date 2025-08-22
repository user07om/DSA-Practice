class ContainsDublicatesII:
    def getDubli(nums: list, k: int) -> bool:
        seen: set = set()  #set the distince container as Set()
        i: int = 0  #set the inital value.
        j: int = 0
        while j < len(nums):  #iterate over the nums range.
            if nums[j] in seen:  # check is index value exist in seen or not., if yes then return true.
                return True

            seen.add(nums[j])

            if j-i>=k:
                seen.remove(nums[i])
                i+=1
            j+=1

        return False


nums = [1, 2, 3, 1]
contDubli = ContainsDublicatesII
print(contDubli.getDubli(nums, 3))
