from typing import List

# =============================================================================
# PRACTICE EXERCISES - Try to implement these yourself first!
# =============================================================================

print("BOOLEAN LOGIC PRACTICE EXERCISES")
print("=" * 50)

# EXERCISE 1: XOR Practice
print("\n📝 EXERCISE 1: XOR Practice")
print("Task: Implement these XOR functions")

def xor_two_values(a: bool, b: bool) -> bool:
    """
    TODO: Implement XOR for two boolean values
    Remember: XOR is True when inputs are DIFFERENT
    
    Examples:
    xor_two_values(True, False) should return True
    xor_two_values(True, True) should return False
    """
    return a ^ b  # not a and b or a and not b  -> it inverse any varable if using ^ 'caret' used for XOR

def xor_multiple_values(values: List[bool]) -> bool:
    """
    TODO: Implement XOR for a list of boolean values
    
    Examples:
    xor_multiple_values([True, False, True]) should return False
    xor_multiple_values([True, False]) should return True
    """
    result = False # set default value.
    for v in values:
        result ^= v   #it will check and assing to result
        # example 
        """
        result is False (whitch itself is a inverse value.)
        and if v is False then it becomes the False output else True if both match the XOR condtion.
        """

    return result
    

# Test cases for Exercise 1
print("Testing XOR functions:")
# Uncomment these lines after implementing the functions
print(f"xor_two_values(True, False) = {xor_two_values(True, False)}")  # Should be True
print(f"xor_multiple_values([True, False, True]) = {xor_multiple_values([True, False, True])}")  # Should be False

print("\n" + "-" * 50)

# EXERCISE 2: Matrix Row Operations
print("\n📝 EXERCISE 2: Matrix Row Operations")
print("Task: Implement these matrix functions")

def count_true_in_row(matrix: List[List[bool]], row_index: int) -> int:
    """
    TODO: Count how many True values are in a specific row
    
    Example:
    matrix = [[True, False, True], [True, True, False]]
    count_true_in_row(matrix, 0) should return 2
    """
    #count = 0
    #for b in matrix[row_index]:
        #if b: count += 1

    result = sum(matrix[row_index])
    return result 

def find_first_all_true_row(matrix: List[List[bool]]) -> int:
    """
    TODO: Find the index of the first row that has ALL True values
    Return -1 if no such row exists
    
    Example:
    matrix = [[True, False], [True, True], [False, True]]
    find_first_all_true_row(matrix) should return 1
    """
#    for v in matrix[1]:
#        if not v:
#            return -1 
    if all(matrix[1]):
        return 1
    return -1

def count_rows_with_any_false(matrix: List[List[bool]]) -> int:
    """
    TODO: Count how many rows contain at least one False value
    
    Example:
    matrix = [[True, True], [True, False], [True, True]]
    count_rows_with_any_false(matrix) should return 1
    """
    count = 0
#    for i in range(len(matrix)):
#        for v in matrix[i]:
#            if not v: 
#                count += 1
#                break
    size = len(matrix[0])
    for i in range(len(matrix)):
        s = sum(matrix[i]) 
        if s != size:
            count += 1
    return count


    


# Test cases for Exercise 2
test_matrix = [
    [True, False, True],   # Row 0: 2 True, has False
    [True, True, True],    # Row 1: 3 True, all True
    [False, False, True],  # Row 2: 1 True, has False
    [True, True, False]    # Row 3: 2 True, has False
]

print("Test matrix:")
for i, row in enumerate(test_matrix):
    print(f"Row {i}: {row}")

# Uncomment these lines after implementing the functions
print(f"True count in row 0: {count_true_in_row(test_matrix, 0)}")  # Should be 2
print(f"First all-true row: {find_first_all_true_row(test_matrix)}")  # Should be 1
print(f"Rows with any False: {count_rows_with_any_false(test_matrix)}")  # Should be 3

print("\n" + "-" * 50)

# EXERCISE 3: Diagonal Operations
print("\n📝 EXERCISE 3: Diagonal Operations")
print("Task: Work with matrix diagonals")

def get_main_diagonal(matrix: List[List[bool]]) -> List[bool]:
    """
    TODO: Extract the main diagonal values (top-left to bottom-right)
    Assume the matrix is square (same number of rows and columns)
    
    Example:
    matrix = [[True, False], [False, True]]
    get_main_diagonal(matrix) should return [True, True]
    """
#    size = len(matrix)-1
#    mid = size+1//2
#    for i in range(len(matrix)):
#        if matrix[0][0] and matrix[mid][mid] and matrix[size][size]:
#            return [matrix[0][0], matrix[mid][mid], matrix[size][size]]
#    return []
    n = len(matrix)
    for i in range(n):
        return matrix[i][i]



def get_anti_diagonal(matrix: List[List[bool]]) -> List[bool]:
    """
    TODO: Extract the anti-diagonal values (top-right to bottom-left)
    
    Example:
    matrix = [[True, False], [False, True]]
    get_anti_diagonal(matrix) should return [False, False]
    """
#    size = len(matrix)-1
#    mid = size+1//2
#    for i in range(len(matrix)):
#        if  not matrix[size][0] and not matrix[mid][mid] and not matrix[0][size] :
#            return [matrix[size][0], matrix[mid][mid], matrix[0][size]]
#
#    return []
    n = len(matrix)
    for i in range(n):
        return matrix[i][n-i-1]


def are_diagonals_equal(matrix: List[List[bool]]) -> bool:
    """
    TODO: Check if main diagonal and anti-diagonal have the same values
    
    Example:
    matrix = [[True, False], [False, True]]
    are_diagonals_equal(matrix) should return False
    """
    # YOUR CODE HERE
    pass

# Test cases for Exercise 3
square_matrix = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]

print("Test square matrix:")
for i, row in enumerate(square_matrix):
    print(f"Row {i}: {row}")

print("Main diagonal should be: [True, True, True]")
print("Anti diagonal should be: [True, True, True]")

# Uncomment these lines after implementing the functions
print(f"Main diagonal: {get_main_diagonal(square_matrix)}")
print(f"Anti diagonal: {get_anti_diagonal(square_matrix)}")
# print(f"Diagonals equal? {are_diagonals_equal(square_matrix)}")

print("\n" + "-" * 50)

# EXERCISE 4: Boolean Array Patterns
print("\n📝 EXERCISE 4: Boolean Array Patterns")
print("Task: Find patterns in boolean arrays")

def has_alternating_pattern(arr: List[bool]) -> bool:
    """
    TODO: Check if array alternates between True and False
    
    Examples:
    has_alternating_pattern([True, False, True, False]) should return True
    has_alternating_pattern([True, True, False]) should return False
    """
    # YOUR CODE HERE
    pass

def longest_consecutive_true(arr: List[bool]) -> int:
    """
    TODO: Find the length of the longest consecutive sequence of True values
    
    Examples:
    longest_consecutive_true([True, True, False, True]) should return 2
    longest_consecutive_true([False, True, True, True, False]) should return 3
    """
    # YOUR CODE HERE
    pass

def find_majority_value(arr: List[bool]) -> bool:
    """
    TODO: Find the boolean value that appears more than half the time
    If there's a tie, return True
    
    Examples:
    find_majority_value([True, True, False]) should return True
    find_majority_value([True, False]) should return True (tie, return True)
    """
    # YOUR CODE HERE
    pass

# Test cases for Exercise 4
test_arrays = [
    [True, False, True, False],      # Alternating
    [True, True, False, True, True], # Longest consecutive True = 2
    [False, False, True, True, True] # Majority = True (3 out of 5)
]

print("Test arrays:")
for i, arr in enumerate(test_arrays):
    print(f"Array {i}: {arr}")

# Uncomment these lines after implementing the functions
# print(f"Array 0 alternating? {has_alternating_pattern(test_arrays[0])}")  # Should be True
# print(f"Array 1 longest consecutive True: {longest_consecutive_true(test_arrays[1])}")  # Should be 2
# print(f"Array 2 majority value: {find_majority_value(test_arrays[2])}")  # Should be True

print("\n" + "=" * 50)
print("🎯 CHALLENGE: Try implementing all functions above!")
print("Start with the easier ones (XOR, counting) and work your way up.")
print("Once you're done, uncomment the test lines to check your solutions!")

# =============================================================================
# HINTS (Don't look unless you're stuck!)
# =============================================================================

"""
HINTS:

Exercise 1 (XOR):
- XOR: use ^ operator or check if values are different
- For multiple values: loop and apply XOR one by one

Exercise 2 (Matrix Rows):
- Use sum() to count True values in a row
- Use all() to check if all values in a row are True
- Use any() to check if any value in a row is False

Exercise 3 (Diagonals):
- Main diagonal: matrix[i][i] for i from 0 to len(matrix)
- Anti diagonal: matrix[i][n-1-i] for i from 0 to len(matrix)

Exercise 4 (Patterns):
- Alternating: compare each element with the previous one
- Consecutive: keep a counter and track the maximum
- Majority: count True values and compare with half the length
"""
