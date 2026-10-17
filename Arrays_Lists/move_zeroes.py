"""
Problem Title: Move Zeroes to the End
LeetCode Reference: Problem #283

Question Description:
---------------------
Given an integer array 'nums', move all 0's to the end of it while maintaining 
the relative order of the non-zero elements. The modification should be done in-place.

Time Complexity: O(n) - Two passes over the data
Space Complexity: O(n) - Uses a temporary array to store non-zero elements
"""

def move_zeroes_brute_force(nums):
    n = len(nums)
    if n <= 1:
        return

    # 1. Ek temporary list banayi saare non-zero elements ko store karne ke liye
    temp = []
    
    # 2. Pehla loop: Har non-zero element ko 'temp' me append karo
    for i in range(0, n):
        if nums[i] != 0:
            temp.append(nums[i])

    n2 = len(temp)
    
    # 3. Dusra loop: Temporary elements ko wapas original array me shuru me daalo
    for i in range(0, n2):
        nums[i] = temp[i]

    # 4. Teesra loop: Bachi hui aakhiri jagahon ko zero se bhar do
    for i in range(n2, n):
        nums[i] = 0
