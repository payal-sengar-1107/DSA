"""
Problem Title: Union of Two Sorted Arrays
Question Description:
---------------------
Given two sorted arrays 'nums1' and 'nums2', merge them into a single sorted array 
containing only unique elements (Union).

Time Complexity: O(n + m) - Single pass through both arrays
Space Complexity: O(n + m) - To store the result array
"""

def find_union(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    result = []
    
    i = 0  # Pointer for nums1
    j = 0  # Pointer for nums2
    
    # Dono arrays ko ek sath compare karte hue chalenge
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            # Duplicate check: agar result khali hai ya current element pichle element jaisa nahi hai
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            # Duplicate check for nums2
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
            
    # Agar nums1 me kuch elements bach gaye hon
    while i < n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
        
    # Agar nums2 me kuch elements bach gaye hon
    while j < m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
        
    return result
