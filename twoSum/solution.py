def twoSum(arr: list, target: int) -> list:
    if len(arr) <= 2:
        return []
    seen: dict = {}
    for i in range(len(arr)):
        compliment = target - arr[i]
        if compliment in seen:
            return [seen[compliment], i]
        
        seen[arr[i]] = i
    
    return []


if __name__ == "__main__":
    """test all aproaches with various test cases."""
    test_cases: list[set[list, int]] = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 8),
        ([5, 5, 5, 5], 10),
        ([-1, -2, -3, -4], -6),
        ([0, 4, 3, 0], 0),
        ([1, 1, 1, 1], 2),
        ([], 5),
        ([1], 1)
    ]

    result: dict = {}
    for i, case in enumerate(test_cases):
        result[i] = twoSum(case[0], case[1])

    print(result)
