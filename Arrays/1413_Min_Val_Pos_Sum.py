### Question
# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by 
# step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum 
# is never less than 1.

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        curr = nums[0] + startValue
        while curr < 1:
            startValue +=1
            curr = nums[0] + startValue
        for i in range(1, len(nums)):
            curr += nums[i]
            if curr < 1:
                add = 1 + abs(curr)
                startValue = startValue + add
                curr += add
                
        return startValue
    
###Solution
# Since the startvalue always has to be one, we can just initialize that.
# In this we will be using something like prefix sum.
# First we ensure that the first number in the list will not be less than one.
# After that we loop through the rest of the list and ensure that the summation of
#     the total is not less than 1. (Look at code abeg)
# Then we just return the startvalue when we are done.