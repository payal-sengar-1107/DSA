Problem Title: Rotate Array Right by One Place
Question Description:
---------------------
Given an array/list of integers 'nums', rotate the array to the right by one position.
The last element of the array should become the first element, and all other elements 
should shift one position to the right. The modification should be done in-place.

Time Complexity: O(n) - Single Pass / Linear Shifting
Space Complexity: O(1) - Constant auxiliary space


def rotate_array_right_slicing(nums):
    """
    Approach 1: Using Python Slicing (Short & Efficient)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    if n <= 1:
        return

  nums[:] = [nums[n - 1]] + nums[0 : n - 1]

def rotate_array_right_loop(nums):
    n = len(nums)
    if n <= 1:
        return

    temp = nums[n - 1]
    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = temp
