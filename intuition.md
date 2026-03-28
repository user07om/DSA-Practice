
# 📘 DAY 1 — Arrays & Basic Logic

## 1. Reverse an array (in-place)
```python
def reverse_array(arr):
    l, r = 0, len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr
````

## 2. Max difference (arr[j] - arr[i]) where j > i

```python
def max_difference(arr):
    min_val = arr[0]
    max_diff = float('-inf')
    for x in arr[1:]:
        max_diff = max(max_diff, x - min_val)
        min_val = min(min_val, x)
    return max_diff
```

## 3. Rotate array right by k

```python
def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]
```

#reverse function approach...

'''
def right_rot(arr, k):
    n = len(arr)
    k %= n
    rev(arr, 0, n-1)
    rev(arr, 0, k-1)
    rev(arr, k, n-1)
    return arr

def left_rot(arr, k):
    n = len(arr)
    k %= n
    rev(arr, 0, n-1) -> [5, 4, 3, 2, 1]
    rev(arr, 0, n-k-1) -> [3, 4, 5, 2, 1]
    rev(arr, n-k, n-1) -> [3, 4, 5, 1, 2]

def rev(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
'''

## 4. All pairs with sum = k, it's like two sum. but we just have to add the pairs to tuple.

```python
def all_pairs_sum(arr, k):
    seen = set()
    pairs = set()
    for num in arr:
        if k - num in seen:
            pairs.add(tuple(sorted((num, k - num))))
        seen.add(num)
    return list(pairs)
```

## 5. Second largest element

```python
def second_largest(arr):
    first = second = float('-inf')
    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    return second
```

---

# 📘 DAY 2 — Prefix, Suffix, Counting

## 6. Suffix sum

```python
def suffix_sum(arr):
    n = len(arr)
    suff = [0]*n
    suff[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        suff[i] = suff[i+1] + arr[i]
    return suff
```

```
def prefix_sum(arr):
    n = len(arr)
    pref = [0]
    for num in arr:
        pref.append(pref[-1]+num)
    
    return pref
```

## 7. Frequency count

```python
def frequency_count(arr):
    mp = {}
    for x in arr:
        mp[x] = mp.get(x, 0) + 1
    return mp
```

## 8. Equilibrium index

```python
def equilibrium_index(arr):
    total = sum(arr)
    left = 0
    for i, x in enumerate(arr):
        if left == total - left - x:
            return i
        left += x
    return -1
```

## 9. Missing number 1..n

```python
def missing_number(arr):
    n = len(arr) + 1
    return n*(n+1)//2 - sum(arr)
```

## 10. Contains duplicates?

```python
def has_duplicates(arr):
    return len(arr) != len(set(arr))
```

---

# 📘 DAY 3 — Sliding Window / Two Pointers

## 11. Count subarrays sum ≤ k

```python
def count_subarrays_leq_k(arr, k):
    count = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s <= k:
                count += 1
    return count
```

## 12. Longest subarray sum ≤ k

```python
def longest_subarray_leq_k(arr, k):
    left = curr = best = 0
    for r in range(len(arr)):
        curr += arr[r]
        while curr > k:
            curr -= arr[left]
            left += 1
        best = max(best, r-left+1)
    return best
```

## 13. Merge sorted arrays

```python
def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            out.append(a[i]); i+=1
        else:
            out.append(b[j]); j+=1
    return out + a[i:] + b[j:]
```

## 14. Pair sum closest to K

```python
def closest_pair_sum(arr, k):
    l, r = 0, len(arr)-1
    closest = float('inf')
    best = ()
    while l < r:
        s = arr[l] + arr[r]
        if abs(k - s) < abs(k - closest):
            closest = s
            best = (arr[l], arr[r])
        if s < k:
            l += 1
        else:
            r -= 1
    return best
```

## 15. Move negative numbers left

```python
def rearrange_neg_pos(arr):
    l = 0
    for r in range(len(arr)):
        if arr[r] < 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    return arr
```

---

# 📘 DAY 4 — Stack / Pattern Recognition

## 16. Balanced parentheses

```python
def is_balanced(s):
    stack = []
    match = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in match.values():
            stack.append(ch)
        elif ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
    return not stack
```

## 17. Next greater element

```python
def next_greater(arr):
    res = [-1]*len(arr)
    stack = []
    for i, x in enumerate(arr):
        while stack and arr[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res
```

## 18. Reverse words

```python
def reverse_words(s):
    return " ".join(s.split()[::-1])
```

## 19. Leaders in array

```python
def find_leaders(arr):
    leaders = []
    max_right = float('-inf')
    for x in reversed(arr):
        if x > max_right:
            leaders.append(x)
            max_right = x
    return leaders[::-1]
```

## 20. Majority element

```python
def majority_element(arr):
    count = 0
    cand = None
    for x in arr:
        if count == 0:
            cand = x
        count += 1 if x == cand else -1
    return cand
```

---

# 📘 DAY 5 — Logic Thinking (Kadane, Prefix tricks)

## 21. Max subarray sum (Kadane)

```python
def max_subarray_sum(arr):
    curr = best = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best
```

## 22. Smallest subarray sum ≥ K

```python
def min_subarray_len(arr, k):
    l = total = 0
    ans = float('inf')
    for r, x in enumerate(arr):
        total += x
        while total >= k:
            ans = min(ans, r-l+1)
            total -= arr[l]
            l += 1
    return ans if ans != float('inf') else 0
```

## 23. Wave array

```python
def wave_array(arr):
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
```

## 24. Product of array except self

```python
def product_except_self(arr):
    n = len(arr)
    prefix = [1]*n
    suffix = [1]*n
    for i in range(1, n):
        prefix[i] = prefix[i-1] * arr[i-1]
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * arr[i+1]
    return [prefix[i] * suffix[i] for i in range(n)]
```

## 25. Longest consecutive sequence

```python
def longest_consecutive(arr):
    nums = set(arr)
    longest = 0
    for x in nums:
        if x-1 not in nums:
            curr = x
            streak = 1
            while curr+1 in nums:
                curr += 1
                streak += 1
            longest = max(longest, streak)
    return longest
```

---

# 📘 DAY 6 — Hashmap / Sets

## 26. First unique element

```python
def first_unique(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    for x in arr:
        if freq[x] == 1:
            return x
    return None
```

## 27. Two Sum

```python
def two_sum(arr, target):
    mp = {}
    for i, x in enumerate(arr):
        if target-x in mp:
            return mp[target-x], i
        mp[x] = i
    return None
```

## 28. Arrays equal (unordered)

```python
def arrays_equal(a, b):
    return frequency_count(a) == frequency_count(b)
```

## 29. Longest substring without repeating

```python
def longest_unique_substring(s):
    seen = set()
    l = best = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        best = max(best, r-l+1)
    return best
```

## 30. Group anagrams

```python
def group_anagrams(words):
    mp = {}
    for w in words:
        key = ''.join(sorted(w))
        mp.setdefault(key, []).append(w)
    return list(mp.values())
```

---

# 📘 DAY 7 — Advanced Intuition

## 31. Buy & sell stock twice

```python
def max_profit_two_transactions(prices):
    buy1 = buy2 = float('inf')
    prof1 = prof2 = 0
    for p in prices:
        buy1 = min(buy1, p)
        prof1 = max(prof1, p - buy1)
        buy2 = min(buy2, p - prof1)
        prof2 = max(prof2, p - buy2)
    return prof2
```

## 32. Trapping rainwater

```python
def trap_rainwater(h):
    l, r = 0, len(h)-1
    left = right = 0
    water = 0
    while l < r:
        if h[l] < h[r]:
            if h[l] >= left:
                left = h[l]
            else:
                water += left - h[l]
            l += 1
        else:
            if h[r] >= right:
                right = h[r]
            else:
                water += right - h[r]
            r -= 1
    return water
```

## 33. Largest rectangle in histogram

```python
def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            L = stack[-1] if stack else -1
            max_area = max(max_area, H*(i-L-1))
        stack.append(i)
    return max_area
```

## 34. Quickselect (kth smallest)

```python
def kth_smallest(arr, k):
    import random
    k -= 1
    def select(lo, hi):
        pivot = arr[random.randint(lo, hi)]
        lows  = [x for x in arr[lo:hi+1] if x < pivot]
        mids  = [x for x in arr[lo:hi+1] if x == pivot]
        highs = [x for x in arr[lo:hi+1] if x > pivot]
        if k < len(lows):
            return select(lo, lo+len(lows)-1)
        elif k < len(lows)+len(mids):
            return pivot
        else:
            return select(lo+len(lows)+len(mids), hi)
    return select(0, len(arr)-1)
```

## 35. Train platforms

```python
def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    i = j = platforms = max_p = 0
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] < departures[j]:
            platforms += 1
            max_p = max(max_p, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    return max_p
```

