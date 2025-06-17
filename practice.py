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


def two_sum_closest_pair(arr: list, target: int) -> list:
    if len(arr) < 2:
        return []
    
    closest_sum = float('inf')
    