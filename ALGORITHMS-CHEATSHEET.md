# 🚀 Algorithms & Data Structures Cheat Sheet
> **Quick Reference Guide for LeetCode & Competitive Programming**
> 
> Use this before every practice session to refresh your mind on key patterns and implementations!

---

## 📊 Time & Space Complexity Quick Reference

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Hash map lookup, array index access |
| O(log n) | Logarithmic | Binary search, balanced tree operations |
| O(n) | Linear | Single loop, array traversal |
| O(n log n) | Linearithmic | Merge sort, quick sort (avg), heap sort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(n³) | Cubic | Triple nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci, subset generation |
| O(n!) | Factorial | Generating all permutations |

---

## 🎯 Common Problem Patterns

| Pattern | When to Use | Key Indicator |
|---------|-------------|---------------|
| **Two Pointers** | Sorted arrays, palindromes | "pair sum", "sorted", "remove duplicates" |
| **Sliding Window** | Subarrays/substrings | "contiguous", "substring", "subarray" |
| **Hash Map/Set** | Tracking frequency, duplicates | "count", "frequency", "find duplicates" |
| **Stack** | Matching pairs, next greater/smaller | "valid parentheses", "next greater" |
| **Queue/BFS** | Level-order, shortest path | "shortest", "level by level" |
| **DFS** | Explore all paths | "all possible", "combinations" |
| **Binary Search** | Sorted data, search space | "sorted", "find minimum/maximum" |
| **Greedy** | Optimal at each step | "maximize", "minimize", "scheduling" |
| **DP** | Overlapping subproblems | "maximum/minimum", "count ways" |
| **Union Find** | Connected components | "connected", "islands", "network" |

---

## 1️⃣ Arrays & Strings

### Reverse Array (In-place)
```python
def reverse_array(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr
```

### Rotate Array by K
```python
def rotate(arr, k):
    n = len(arr)
    k %= n  # Handle k > n
    # Reverse entire, reverse first k, reverse rest
    arr[:] = arr[-k:] + arr[:-k]
    return arr
```

### Find Max/Min in Array
```python
def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
    return max_val, min_val
```

### Kadane's Algorithm (Max Subarray Sum)
```python
def max_subarray_sum(arr):
    curr_sum = max_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

### Product of Array Except Self
```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Forward pass
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Backward pass
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result
```

### Missing Number (1 to n)
```python
def missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)
```

### Find Duplicates
```python
def find_duplicates(arr):
    seen = set()
    duplicates = []
    for num in arr:
        if num in seen:
            duplicates.append(num)
        seen.add(num)
    return duplicates
```

### String Reversal
```python
def reverse_string(s):
    return s[::-1]

def reverse_words(s):
    return ' '.join(s.split()[::-1])
```

### Check Palindrome
```python
def is_palindrome(s):
    # Clean string: lowercase, alphanumeric only
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

### Longest Substring Without Repeating Characters
```python
def longest_unique_substring(s):
    char_set = set()
    left = max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

---

## 2️⃣ Two Pointers

### Two Sum (Sorted Array)
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

### Three Sum (Find Triplets = 0)
```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

### Remove Duplicates from Sorted Array
```python
def remove_duplicates(arr):
    if not arr:
        return 0
    
    write_ptr = 1
    for read_ptr in range(1, len(arr)):
        if arr[read_ptr] != arr[read_ptr - 1]:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1
    
    return write_ptr
```

### Container With Most Water
```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

---

## 3️⃣ Sliding Window

### Fixed Size Window (Max Sum of Size K)
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Variable Size Window (Longest Subarray Sum ≤ K)
```python
def longest_subarray_sum_leq_k(arr, k):
    left = curr_sum = max_len = 0
    
    for right in range(len(arr)):
        curr_sum += arr[right]
        
        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### Minimum Window Substring
```python
def min_window_substring(s, t):
    from collections import Counter
    
    if not s or not t:
        return ""
    
    target_count = Counter(t)
    required = len(target_count)
    formed = 0
    window_counts = {}
    
    left = 0
    min_len = float('inf')
    min_left = 0
    
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_count and window_counts[char] == target_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            
            char = s[left]
            window_counts[char] -= 1
            if char in target_count and window_counts[char] < target_count[char]:
                formed -= 1
            left += 1
    
    return "" if min_len == float('inf') else s[min_left:min_left + min_len]
```

---

## 4️⃣ Hash Map & Hash Set

### Two Sum (Unsorted)
```python
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Group Anagrams
```python
def group_anagrams(strs):
    from collections import defaultdict
    
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())
```

### First Non-Repeating Character
```python
def first_unique_char(s):
    from collections import Counter
    
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
```

### Longest Consecutive Sequence
```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            current = num
            streak = 1
            
            while current + 1 in num_set:
                current += 1
                streak += 1
            
            longest = max(longest, streak)
    
    return longest
```

### Subarray Sum Equals K
```python
def subarray_sum_k(nums, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix_sum: frequency
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

---

## 5️⃣ Stack

### Valid Parentheses
```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack
```

### Next Greater Element
```python
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []  # Store indices
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    
    return result
```

### Daily Temperatures
```python
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []  # Store indices
    
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result
```

### Min Stack (O(1) getMin)
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
```

### Evaluate Reverse Polish Notation
```python
def eval_rpn(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                # Truncate toward zero
                stack.append(int(a / b) if a * b >= 0 else -int(-a / b))
        else:
            stack.append(int(token))
    
    return stack[0]
```

---

## 6️⃣ Linked List

### Linked List Node Definition
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Reverse Linked List
```python
def reverse_list(head):
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev
```

### Detect Cycle (Floyd's Algorithm)
```python
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
```

### Find Middle of Linked List
```python
def find_middle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

### Merge Two Sorted Lists
```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 or l2
    return dummy.next
```

### Remove Nth Node From End
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    
    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next
    
    # Move both until fast reaches end
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    # Remove the node
    slow.next = slow.next.next
    return dummy.next
```

---

## 7️⃣ Binary Trees

### Tree Node Definition
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Inorder Traversal (Left → Root → Right)
```python
def inorder(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    
    traverse(root)
    return result
```

### Preorder Traversal (Root → Left → Right)
```python
def preorder(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
    
    traverse(root)
    return result
```

### Postorder Traversal (Left → Right → Root)
```python
def postorder(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
    
    traverse(root)
    return result
```

### Level Order Traversal (BFS)
```python
def level_order(root):
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### Max Depth of Binary Tree
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### Check if Balanced Tree
```python
def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1
```

### Lowest Common Ancestor (BST)
```python
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

### Validate BST
```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))
```

---

## 8️⃣ Recursion & Backtracking

### Fibonacci
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Optimized with memoization
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

### Generate Permutations
```python
def permutations(nums):
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    backtrack([], nums)
    return result
```

### Generate Subsets
```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```

### Generate Combinations
```python
def combinations(n, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(1, [])
    return result
```

### Letter Combinations of Phone Number
```python
def letter_combinations(digits):
    if not digits:
        return []
    
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return
        
        for letter in mapping[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```

---

## 9️⃣ Sorting Algorithms

### Quick Sort
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
```

### Merge Sort
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Heap Sort
```python
def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

### Counting Sort (for small range integers)
```python
def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    for num in arr:
        count[num - min_val] += 1
    
    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)
    
    return result
```

---

## 🔟 Binary Search

### Classic Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### Find First Occurrence
```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Find Last Occurrence
```python
def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Search in Rotated Sorted Array
```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

### Find Peak Element
```python
def find_peak_element(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left
```

---

## 1️⃣1️⃣ Dynamic Programming Basics

### Climbing Stairs (n steps, 1 or 2 at a time)
```python
def climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

### House Robber
```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2, prev1 = 0, 0
    
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr
    
    return prev1
```

### Coin Change (Min coins to make amount)
```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

### Longest Increasing Subsequence
```python
def length_of_lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

### 0/1 Knapsack
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]
```

---

## 1️⃣2️⃣ Graph Algorithms Basics

### Graph Representation
```python
# Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

### DFS (Depth First Search)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result
```

### BFS (Breadth First Search)
```python
def bfs(graph, start):
    from collections import deque
    
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

### Number of Islands (DFS)
```python
def num_islands(grid):
    if not grid:
        return 0
    
    count = 0
    
    def dfs(i, j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or 
            grid[i][j] == '0'):
            return
        
        grid[i][j] = '0'  # Mark as visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    
    return count
```

### Detect Cycle in Directed Graph
```python
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    
    def dfs(node):
        if color[node] == GRAY:
            return True  # Back edge found
        if color[node] == BLACK:
            return False
        
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        color[node] = BLACK
        return False
    
    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    return False
```

---

## 🎓 Common Tricks & Edge Cases

### Python Built-ins That Save Time
```python
# Sorting with custom key
arr.sort(key=lambda x: (x[0], -x[1]))  # Sort by first asc, second desc

# Counter for frequency
from collections import Counter
freq = Counter(arr)

# Default dict
from collections import defaultdict
graph = defaultdict(list)

# Deque for O(1) popleft
from collections import deque
queue = deque()

# Heapq for min heap
import heapq
heap = []
heapq.heappush(heap, item)
heapq.heappop(heap)

# Bisect for binary search
import bisect
idx = bisect.bisect_left(arr, target)

# Set operations
set1 & set2  # Intersection
set1 | set2  # Union
set1 - set2  # Difference
```

### Common Edge Cases to Check
```python
# Empty input
if not arr or len(arr) == 0:
    return []

# Single element
if len(arr) == 1:
    return arr[0]

# All same elements
if len(set(arr)) == 1:
    return arr[0]

# Negative numbers
# Handle negative indices, sums, products

# Integer overflow
# Use float('inf') or check bounds

# Duplicates
# Use set or track frequency

# Sorted vs Unsorted
# Sorting can reduce O(n²) to O(n log n)
```

### Avoid Integer Overflow
```python
# Mid point calculation
mid = left + (right - left) // 2  # Instead of (left + right) // 2
```

### Fast I/O in Python (for competitive programming)
```python
import sys
input = sys.stdin.readline

# Reading integers
n = int(input())
arr = list(map(int, input().split()))
```

---

## 🔥 Quick Mental Checklist Before Coding

1. **Understand the problem**
   - What are inputs/outputs?
   - What are constraints (size, range)?
   - Any special edge cases mentioned?

2. **Identify the pattern**
   - Does sorting help?
   - Is it a sliding window problem?
   - Can I use hash map for O(1) lookup?
   - Is recursion/backtracking needed?

3. **Think about complexity**
   - What's brute force? O(n²), O(n³)?
   - Can I do better? O(n log n), O(n)?
   - Space trade-off?

4. **Handle edge cases**
   - Empty input
   - Single element
   - All same
   - Negative numbers
   - Integer overflow

5. **Code & test**
   - Start with simple solution
   - Test with examples
   - Trace through logic
   - Optimize if needed

---

## 📝 Practice Strategy

1. **Warm-up (5 mins)**: Review this cheat sheet
2. **Start Easy**: Build confidence with 1-2 easy problems
3. **Level Up**: Move to medium problems
4. **Learn Patterns**: When stuck, identify the pattern first
5. **Time Yourself**: Practice under time constraints
6. **Review**: After solving, review better solutions
7. **Track Progress**: Keep a log of problems solved

---

## 🏆 Final Tips

- **Don't memorize, understand the pattern**
- **Practice regularly** (consistency > intensity)
- **Learn from mistakes** (review wrong answers)
- **Time management** (know when to move on)
- **Communication** (explain your approach in interviews)
- **Test thoroughly** (edge cases matter!)

---

> **Remember**: Every expert was once a beginner. Keep practicing! 🚀
