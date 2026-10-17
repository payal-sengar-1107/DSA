"""
Problem Title: Missing Number
LeetCode Reference: Problem #268

Question Description:
---------------------
Given an array 'nums' containing 'n' distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Time Complexity: O(n) - For the Optimal Approach
Space Complexity: O(1) - For the Optimal Approach
"""

def find_missing_number_brute(nums):
    """
    Approach 1: Brute Force (Using 'in' operator check)
    Time Complexity: O(n^2) - Loop runs n times, and 'if i not in nums' takes O(n) each time
    Space Complexity: O(1)
    """
    n = len(nums)
    
    # Range 0 se n tak har number ko check karenge
    for i in range(0, n + 1):
        if i not in nums:
            return i
            
    return -1


def find_missing_number_better(nums):
    """
    Approach 2: Better Approach (Using Dictionary / Frequency Map)
    Time Complexity: O(n) - Linear scan
    Space Complexity: O(n) - Extra memory used by dictionary
    """
    n = len(nums)
    freq = {}
    
    # Shuruat me saare range ke numbers ki frequency 0 set ki
    for i in range(0, n + 1):
        freq[i] = 0
        
    # Jo numbers array me hain unki frequency 1 kar di
    for num in nums:
        freq[num] = 1
        
    # Jiski frequency 0 reh gayi, wahi missing number hai
    for k, v in freq.items():
        if v == 0:
            return k
            
    return -1


def find_missing_number_optimal(nums):
    """
    Approach 3: Optimal Approach (Using Sum Formula)
    Time Complexity: O(n) - Single loop to find actual sum
    Space Complexity: O(1) - Constant auxiliary space
    """
    n = len(nums)
    
    # 1. Sum formula se 0 se n tak ka total expected sum nikala
    expected_sum = (n * (n + 1)) // 2
    
    # 2. Array ke andar maujood saare elements ka actual sum nikala
    actual_sum = sum(nums)
    
    # 3. Expected sum me se Actual sum minus karte ہی missing number mil jayega
    return expected_sum - actual_sum
