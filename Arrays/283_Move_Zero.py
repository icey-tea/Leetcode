###Question
# Given an integer array nums, move all 0's to the end of it while maintaining the 
# relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        if len(nums) == 1:
            return nums
        while j < len(nums):
            if nums[i] == 0 and nums[j] == 0:
                j+=1
            elif nums[i] == 0 and nums[j]!=0:
                nums[i] , nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            else:
                i+=1
                j+=1

###Solution
# Use and initialize two pointers, placing one pointer one index forward(j)
# First check if the list has only one element and just return it
# Then if not
#     we check if the i and j are Zero(0)
#         if yes then we move j+=1
#     if i in a zero and j is a not 
#         then we switch nums[i] and nums[j]
#         and we increment i and j by one 
#     else 
#         we just increment i and j by one