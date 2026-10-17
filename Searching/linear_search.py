"""
Problem Title: Linear Search
Question Description:
---------------------
Given an array 'nums' and a 'target' value, search for the target in the array.
If the target exists, return its index. Otherwise, return -1.

Time Complexity: O(n) - Linear time
Space Complexity: O(1) - Constant space
"""

def linear_search(nums, target):
    n = len(nums)
    
    # Poore array me ek-ek karke element check karenge
    for i in range(0, n):
        if nums[i] == target:
            return i  # Target milte hi uska index return kar do
            
    return -1  # Agar poora loop chal gaya aur target nahi mila
