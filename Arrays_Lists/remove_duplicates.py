Problem Title: Remove Duplicates from Sorted Array
Question Description:
---------------------
Given an integer array 'nums' sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should be kept the same.
Return the number of unique elements in the array.

Time Complexity: O(n) - Single Pass (Two-pointer technique)
Space Complexity: O(1) - In-place modification (No extra space used)


def remove_duplicates(nums):
    n = len(nums)
    
    # Agar array khali hai ya usme sirf 1 element hai, to koi duplicate nahi ho sakta
    if n <= 1:
        return n

    # 'i' pointer unique elements ki positions ko track karega
    i = 0
    
    # 'j' pointer poore array ko scan karega
    j = 1
    
    while j < n:
        # Jab hume koi naya (unique) element milta hai
        if nums[j] != nums[i]:
            i += 1             # Unique position ko ek aage badhao
            nums[i] = nums[j]  # Naye unique element ko sahi jagah par copy karo
        
        j += 1  # Har baar j ko aage badhate rahenge

    # Unique elements ka total count 'i + 1' hoga kyunki indexing 0 se start hoti hai
    return i + 1
