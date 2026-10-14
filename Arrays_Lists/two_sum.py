# PROBLEM: 1. Two Sum (LeetCode)
# 
# DESCRIPTION:
# Given an array of integers 'nums' and an integer 'target', return indices of 
# the two numbers such that they add up to 'target'.
# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.
# 
# EXAMPLE:
# Input: nums =, target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store numbers and their corresponding indices
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If complement is found, return the indices
            if complement in num_map:
                return [num_map[complement], i]
                
            # Otherwise, store the current number and its index
            num_map[num] = i
