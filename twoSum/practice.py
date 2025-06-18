from collections import defaultdict
def twoSum_br_f(arr: list[int], target: int) -> list[int]:
    """Brute Force approch: TC = O(n*2), SC: O(1)"""
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return []
    

def twoSum_hashmap(arr: list[int], target: int) -> list[int]:
    """Hash Map approch: TC: O(n), SC: O(n)"""
    seen: dict = {}
    for i, num in enumerate(arr):
        compliment: int = target - num
        if compliment in seen:
            return [seen[compliment], i]
        seen[num] = i
    return []


#the default twoSum adds only first occurences that add up to the target value
#but in this version it add all the pairs that addup to the target value.
def two_sum_all_pairs_hashmap(arr: list, target: int) -> list[list[int]]:
    result: list = [] #empty list for stroring the list
    seen: dict = {} #dict
    for i in range(len(arr)):
        compliment: int = target - arr[i]
        # print(compliment)
        if compliment in seen:
            for idx in seen[compliment]:
                result.append([idx, i])

        if arr[i] not in seen:
            seen[arr[i]] = []
        seen[arr[i]].append(i)

    return result

# print(two_sum_all_pairs_hashmap([5, 4, 2, 3], 7))
def two_sum_count_pairs(arr: list, target: int) -> int:
    count = 0
    seen: dict = defaultdict(int)
    for num in arr:
        compliment = target - num
        count += seen[compliment]
        seen[num] += 1

    return count


def two_sum_count_pairs_bs(arr: list, target: int) -> int:
    count = 0
    seen = defaultdict(int)
    for n in arr:
        compliment = target - n
        count += seen[compliment]
        seen[n] += 1

    return count

# print(two_sum_count_pairs_bs([5, 9, 2, 8], 7))


def two_sum_closest_pair_min_method(arr: list, target: int) -> list:
    if len(arr) < 2:
        return []
    
    closest_sum = float('inf')
    seen = {}
    for i in range(len(arr)):
        num = arr[i]
        compliment = target - num
        if compliment in seen:
            closest_sum = min(closest_sum, num + seen[compliment])
        seen[num] = num

    return closest_sum

def two_sum_closest_pair(arr: list, target: int) -> list:
    """
    This function takes an array of integers and a target value and returns the pair of indices
    of the two elements in the array which sum is closest to the target value.
    """
    if len(arr) < 2:
        return []

    # Initialize the result list and the seen dictionary
    result = []
    seen = {}

    # Initialize the closest sum as a very large number
    closest_sum = 0

    # Loop through the array and for each element, loop through the seen dictionary
    # and check if there is a pair of elements which sum is closer to the target
    # than the current closest sum
    for i in range(len(arr)):
        for prev_n, prev_i in seen.items():
            current_sum = prev_n + arr[i]

            # If the current sum is closer to the target than the current closest sum
            # then update the closest sum and the result list
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                result.append([prev_i, i])

        # Add the current element to the seen dictionary
        seen[arr[i]] = i

    # Return the result list
    return result

print(two_sum_closest_pair([1, 2, 3, 5], 4))


def freq_twoSum(arr: list, target: int) -> bool:
    freq: dict = {}
    result: list = []
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in freq:
        compliment = target - num
        if compliment in freq:
            result.append([compliment, num])
            print(freq)
            print(result)
            if freq[num] >= 2:
                return True

    return False 

print(freq_twoSum([3, 1, 1, 3, 1, 8, 9], 4))


def dubli_twoSum(arr: list, target: int) -> list[list[int]]:
    if len(arr) < 2:
        return []
    
    result: list = list()
    visited: set =  set()
    indices_grp = defaultdict(list)

    for num in range(len(arr)):
        indices_grp[arr[num]].append(num)
    print(nums)
    print(list(indices_grp.values()))

    for num in indices_grp:
        compliment = target - num   
        if compliment in indices_grp and (num, compliment) not in visited:
            for i in indices_grp[num]:
                for j in indices_grp[compliment]:
                    if i < j:
                        result.append([i, j])   
        visited.add((num, compliment))
    return result

nums: list = [3, 1, 3, 2, 2, 2, 2]
target: int = 4
lets_see = dubli_twoSum(nums, target)
print(lets_see)

