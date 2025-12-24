# Array Patterns & Practice Problems

## Core Array Techniques (Master These First!)

### 1. Two Pointers Pattern

**Concept:** Use two pointers moving through the array in different ways.

**Variations:**
- **Easy:** Two pointers from both ends (converging)
- **Medium:** Fast and slow pointers (same direction)
- **Hard:** Three pointers for complex conditions

**Practice Problems:**
- Two Sum II (sorted array)
- Remove Duplicates from Sorted Array
- Container With Most Water
- 3Sum

**Key Boolean Logic:**
- `left < right` (boundary condition)
- `nums[left] + nums[right] == target` (condition check)
- `while left < right and nums[left] == nums[left+1]` (skip duplicates)

---

### 2. Sliding Window

**Concept:** Maintain a window of elements that satisfies certain conditions.

**Variations:**
- **Easy:** Fixed-size window
- **Medium:** Variable-size window with conditions
- **Hard:** Multiple windows or complex conditions

**Practice Problems:**
- Maximum Average Subarray (fixed window)
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Sliding Window Maximum

**Key Boolean Logic:**
- `window_size == k` (fixed window check)
- `is_valid_window()` (custom condition)
- `while condition_violated` (shrink window)

---

### 3. Prefix Sum / Running Sum

**Concept:** Precompute cumulative sums for O(1) range queries.

**Variations:**
- **Easy:** Simple prefix sum array
- **Medium:** Prefix sum with hash map
- **Hard:** 2D prefix sum (matrix)

**Practice Problems:**
- Running Sum of 1d Array
- Subarray Sum Equals K
- Range Sum Query
- Product of Array Except Self (variation)

**Key Boolean Logic:**
- `prefix[i] - prefix[j] == target` (subarray sum check)
- `sum in hash_map` (existence check)

---

### 4. In-Place Array Manipulation

**Concept:** Modify array without using extra space.

**Variations:**
- **Easy:** Simple swapping/rearranging
- **Medium:** Cyclic replacements
- **Hard:** Complex state tracking

**Practice Problems:**
- Move Zeroes
- Rotate Array
- Sort Colors (Dutch National Flag)
- First Missing Positive

**Key Boolean Logic:**
- `nums[i] == 0` (condition to move)
- `i != j` (swap condition)
- Boolean flags for visited elements

---

### 5. Array Sorting Patterns

**Concept:** Use sorting to simplify problem logic.

**Variations:**
- **Easy:** Sort and simple iteration
- **Medium:** Sort with two pointers
- **Hard:** Custom sorting with comparators

**Practice Problems:**
- Merge Intervals
- Meeting Rooms
- Largest Number
- Sort Colors (without sorting)

**Key Boolean Logic:**
- `intervals[i][1] >= intervals[i+1][0]` (overlap check)
- Custom comparators with boolean returns

---

### 6. Hash Map / Hash Set with Arrays

**Concept:** Use hash structures for O(1) lookups.

**Variations:**
- **Easy:** Simple existence checking
- **Medium:** Frequency counting
- **Hard:** Complex state mapping

**Practice Problems:**
- Two Sum
- Longest Consecutive Sequence (you solved this!)
- Group Anagrams
- Top K Frequent Elements

**Key Boolean Logic:**
- `num in hash_set` (O(1) membership test)
- `count >= k` (frequency threshold)

---

### 7. Array Partitioning

**Concept:** Divide array into sections based on conditions.

**Variations:**
- **Easy:** Partition by single condition
- **Medium:** Three-way partitioning
- **Hard:** Multiple partition criteria

**Practice Problems:**
- Partition Array
- Sort Colors (3-way partition)
- Partition Equal Subset Sum
- Quick Select

**Key Boolean Logic:**
- `nums[i] < pivot` (partition condition)
- Boolean flags for partition boundaries

---

### 8. Kadane's Algorithm (Subarray Problems)

**Concept:** Find optimal subarray using dynamic state.

**Variations:**
- **Easy:** Maximum subarray sum
- **Medium:** Maximum product subarray
- **Hard:** Multiple constraints on subarray

**Practice Problems:**
- Maximum Subarray
- Maximum Product Subarray
- Best Time to Buy and Sell Stock
- Maximum Sum Circular Subarray

**Key Boolean Logic:**
- `current_sum > 0` (should continue or restart)
- `num < 0` (special handling for negatives)

---

### 9. Binary Search on Arrays

**Concept:** Use binary search for sorted or rotated arrays.

**Variations:**
- **Easy:** Standard binary search
- **Medium:** Search in rotated array
- **Hard:** Binary search on answer space

**Practice Problems:**
- Binary Search
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Search a 2D Matrix

**Key Boolean Logic:**
- `mid < target` (search direction)
- `nums[mid] > nums[right]` (rotation detection)
- `left <= right` (loop boundary)

---

### 10. Array with Boolean Flags

**Concept:** Use boolean arrays to track states.

**Variations:**
- **Easy:** Simple visited array
- **Medium:** Multiple state tracking
- **Hard:** Boolean array optimization

**Practice Problems:**
- Find All Numbers Disappeared in Array
- Set Matrix Zeroes
- Game of Life
- Valid Sudoku

**Key Boolean Logic:**
- `visited[i] = True/False`
- `seen[num] = True` (mark as seen)
- `is_valid[row][col]` (validity checking)

---

## 🎯 Learning Path (Recommended Order)

### Week 1-2: Basics
1. Two Pointers (easiest to understand)
2. Hash Map with Arrays
3. In-Place Manipulation

### Week 3-4: Intermediate
4. Sliding Window
5. Prefix Sum
6. Array Sorting Patterns

### Week 5-6: Advanced
7. Array Partitioning
8. Kadane's Algorithm
9. Binary Search on Arrays
10. Boolean Flags (advanced usage)

---

## 🧠 Boolean Logic Patterns in Arrays

### Pattern 1: Boundary Conditions
```python
# Always check array bounds
if not nums or len(nums) == 0:
    return result

if i < 0 or i >= len(nums):
    return False
```

### Pattern 2: Index Comparison
```python
# Compare indices, not values (common mistake!)
if i != j:  # ✅ Correct
if nums[i] != nums[j]:  # ❌ Wrong for certain problems
```

### Pattern 3: Value Existence
```python
# Use sets for O(1) lookups
if target in num_set:  # ✅ O(1)
if target in nums:     # ❌ O(n)
```

### Pattern 4: Range Checks
```python
# Multiple conditions with short-circuit
if left < right and nums[left] < target:
    # left < right checked first (safety)
```

### Pattern 5: State Flags
```python
# Track multiple states with booleans
found = False
is_sorted = True
has_duplicates = False
```

---

## 📝 Practice Strategy

### For Each Pattern:
1. **Solve 2-3 Easy problems** to understand the pattern
2. **Solve 2-3 Medium problems** to master variations
3. **Solve 1 Hard problem** to challenge yourself
4. **Focus on understanding 1-2 approaches deeply** per problem

### Daily Practice Routine:
- **Day 1-2**: Learn pattern + solve 2 easy
- **Day 3-4**: Solve 2 medium problems
- **Day 5**: Solve 1 hard problem
- **Day 6**: Review and solve variations
- **Day 7**: Rest or solve mixed problems

---

## 🔥 Most Important Patterns for Interviews

**Top 5 (Master These First!):**
1. **Two Pointers** - appears in 30% of array problems
2. **Hash Map** - appears in 25% of array problems
3. **Sliding Window** - appears in 20% of array problems
4. **Prefix Sum** - appears in 15% of array problems
5. **In-Place Manipulation** - appears in 10% of array problems

---

## 💡 Common Boolean Logic Mistakes in Arrays

1. **Off-by-one errors**: `i < len(nums)` vs `i <= len(nums)`
2. **Index vs Value**: Comparing `i == j` vs `nums[i] == nums[j]`
3. **Short-circuit order**: Check safer conditions first
4. **Empty array**: Always check `if not nums`
5. **Integer overflow**: In languages like C++/Java (Python handles this)

---

## 🎓 Pro Tips

1. **Draw it out**: Visualize array manipulations on paper
2. **Test edge cases**: Empty array, single element, all same elements
3. **Time yourself**: Try to solve in 20-30 minutes
4. **Explain out loud**: Practice explaining your approach
5. **Code clean first**: Don't optimize prematurely

---

## 🚀 Next Steps

After mastering arrays, these data structures use similar patterns:
- **Strings** (very similar to arrays)
- **Linked Lists** (uses two pointers heavily)
- **Stacks/Queues** (uses array-like thinking)
- **Trees** (applies array traversal concepts)

Would you like me to create similar guides for any of these topics?
