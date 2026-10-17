"""
Problem Title: Check if Array is Sorted
Question Description:
---------------------
Given an array/list of integers 'nums', check if the array is sorted in non-decreasing (ascending) order. 
If the array is sorted, return True. Otherwise, return False.

Time Complexity: O(n) - Single Pass
Space Complexity: O(1) - Constant Space
"""

def is_array_sorted(nums):
    n = len(nums)
    
    # Empty array ya single element array hamesha sorted hota hai
    if n <= 1:
        return True

    # Array ko check karenge ki koi element apne agle se bada to nahi hai
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False  # Sorted nahi hai
            
    return True  # Sorted hai
