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



"""
Problem Title: Move Zeroes to the End
LeetCode Reference: Problem #283 (Optimal Solution)

Question Description:
---------------------
Given an integer array 'nums', move all 0's to the end of it while maintaining 
the relative order of the non-zero elements. The modification must be done in-place.

Time Complexity: O(n) - Single Pass (Two-pointer approach)
Space Complexity: O(1) - Constant auxiliary space (No extra space used)
"""

def move_zeroes_optimal(nums):
    n = len(nums)
    if n <= 1:
        return

    # 1. Pehle zero element ka index dhoondho
    i = 0
    while i < n:
        if nums[i] == 0:
            break
        i += 1

    # Agar array me koi zero mila hi nahi, to return kar jao
    if i == n:
        return

    # 2. 'j' pointer ko pehle zero ke theek baad se shuru karo
    j = i + 1
    
    while j < n:
        # Agar 'j' index par koi non-zero element milta hai, to use 'i' ke zero se swap karo
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1  # Swap karne ke baad 'i' ko agle zero element par badhao
            
        j += 1  # 'j' har baar aage badhta rahega non-zero ki talash me
