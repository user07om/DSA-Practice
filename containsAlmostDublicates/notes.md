## 💡 Daily Log Template
# Date: 2025-07-16
# Problem: containsAlmostDublicates
# Difficulty: Easy 
# Language: Python, JS
# Concepts: 
# Time taken: ___ mins

## Summary:
- we have given the nums array and two integer as indexDiff and valueDiff
- return the boolean value. following are the contraints.
    1. if the element is dublicate found, check its abs val of it index distance should be less than equal to k means (indexDiff) abs(i-j)<=indexDiff
    2. if the element is dublicate found, check its abs val of its element is less than queal to k means (valueDiff) 
    abs(nums[i]-nums[j])<=valueDiff 
    3. and i should not equal to j, means it's index's should be not equal to each other (i!=j)

## Pseudocode:
    - BruteForch Approach
        1. BruteForch approach would be two loops as bubble sort algo
        2. outer loop would iterate over the arr
        3. inner loop will iterate over the second element as start from i+1 till len(arr)
        4. condition sould be - outer loop is i and inner is j so check add more above contraints to it. and if all condition match return True and at end of function return False.
    - Optimal Approach
        1. use the hashmap.


## Learnings:

## Mistakes:


## Tags:
