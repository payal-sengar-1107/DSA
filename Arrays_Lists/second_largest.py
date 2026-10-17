"""
Problem Title: Find the Second Largest Element in an Array

Question Description:
---------------------
Given an array of integers 'nums', find the second largest element in the array. 
If the second largest element does not exist (e.g., if all elements are equal or 
the array size is less than 2), return -1.

Example:
--------
Input: nums = [55, 32, 97, -53, 45, 32, 80, 21]
Output: 80
Explanation: The largest element is 97, and the second largest element is 80.

Time Complexity: O(n) - Single Pass (Only one loop)
Space Complexity: O(1) - Constant Space
"""

def find_second_largest(nums):
    n = len(nums)
    if n < 2:
        return -1

    # Dono variables ko minus infinity se initialize kiya
    largest = float('-inf')
    s_largest = float('-inf')

    # Ek hi loop me poora array scan karenge (Single Pass)
    for i in range(0, n):
        # Condition 1: Agar current element ab tak ke 'largest' se bhi bada hai
        if nums[i] > largest:
            s_largest = largest  # Purana largest ab second largest ban gaya
            largest = nums[i]    # Naya largest update ho gaya

        # Condition 2: Agar element 'largest' se chota hai par 's_largest' se bada hai
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]  # Second largest ko update kiya

    # Agar s_largest change nahi hua, matlab koi second largest nahi mila
    if s_largest == float('-inf'):
        return -1
        
    return s_largest
