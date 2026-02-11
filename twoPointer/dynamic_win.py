#smallest subarray with sum >= target

def smallest_sub(arr: list[int], target: int) -> int:
    """
	smallest subarray with sum >= target:
	we declare three variables left, min_sum and curr_sum.
	iterate over the array - as left pointer.
	we add the we add the right elements to the curr_sum,
	and at end we compare curr_window length and min_len
	between those we add the while loop, that until the curr_sum >= target:
	"""
    left = 0
    min_len = float("inf")
    win_sum = 0 

    for right in range(len(arr)):
        win_sum += arr[right]

        while win_sum >= target:
            min_len = min(min_len, right-left+1)

            win_sum -= arr[left]
            left += 1


    return min_len 

print("smallest subarray with sum >= target: ", smallest_sub([2, 3, 1, 2, 4, 3], 7))


#longest subarray with sum <= target
def long_sub(arr: list[int], target: int) -> int:
    left = 0
    max_len = float("-inf")
    curr_sum = 0

    for right in range(len(arr)):
        curr_sum += arr[right]

        while curr_sum == target:
            curr_sum -= arr[left]
            left += 1

        max_len = max(max_len, (right-left)+1)

    return max_len

print("longest subarray with sum gte target: ", long_sub([1, 2, 1, 0, 1, 1, 0], 4))


#longest subarray without repeating the character.
def long_sub_s(s: str) -> int:
    """
    
    """
    left = 0
    seen = set()
    max_len = float("-inf")

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, (right-left)+1)

    return max_len 

print(long_sub_s("bbbbb"))


#longest substring with atmost k distinct characters.
def long_str(s: str, k: int) -> int:
    left = 0
    max_len = 0
    seen = {}
    for right in range(len(s)):
        char = s[right]
        seen[char] = seen.setdefault(char, 0)+1

        
        while len(seen) > k:
            char_left = s[left]
            seen[char_left] -= 1
            if seen[char_left] == 0:
                del seen[char_left]
            left += 1

        max_len = max(max_len, (right-left)+1)

    return max_len


print("fuckkkk...", long_str("aaaa", 1))

