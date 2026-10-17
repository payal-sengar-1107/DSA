"""
Problem Title: Rotate Array Right by K Places
Question Description:
---------------------
Given an array/list of integers 'nums', rotate the array to the right by 'k' steps, 
where 'k' is a non-negative integer. The modification should be done in-place.

Time Complexity: O(n) - Optimal Reversal Method
Space Complexity: O(1) - Constant auxiliary space
"""

def rotate_array_k_brute(nums, k):
    """
    Approach 1: Brute Force (Using pop() and insert())
    Time Complexity: O(k * n) - pop() from end is O(1) but insert(0) shifts elements taking O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    if n <= 1:
        return
        
    # K agar array size se bada hai to wrap around karenge
    rotation = k % n
    
    # Loop chala kar ek-ek element ko aakhiri se uthakar aage insert karenge
    for _ in range(rotation):
        e = nums.pop()        # O(1)
        nums.insert(0, e)     # O(n) -> total loop cost: O(k * n)


def rotate_array_k_better(nums, k):
    """
    Approach 2: Better Approach using Slicing
    Time Complexity: O(n) - Shifting slices takes linear time
    Space Complexity: O(1) - Python slice assignment is optimized in-place
    """
    n = len(nums)
    if n <= 1:
        return
        
    k = k % n
    
    # Copy me likha tarika: nums[:] = nums[n-k:] + nums[:n-k]
    nums[:] = nums[n - k :] + nums[: n - k]


def rotate_array_k_optimal(nums, k):
    """
    Approach 3: Optimal Approach (Reversal Algorithm)
    Time Complexity: O(n) - reversing parts takes linear time overall
    Space Complexity: O(1) - Constant auxiliary space (No slicing, true in-place)
    """
    n = len(nums)
    if n <= 1:
        return
        
    k = k % n

    # Helper function ek custom range me array ko ulta (reverse) karne ke liye
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Step 1: Aakhiri ke K elements ko ulta karo
    reverse(n - k, n - 1)
    
    # Step 2: Shuruat ke bache hue (n-k) elements ko ulta karo
    reverse(0, n - k - 1)
    
    # Step 3: Pure array ko ek sath dobara ulta karke sahi position par lao
    reverse(0, n - 1)
