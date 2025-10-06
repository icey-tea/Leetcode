###Question
# Given an array of positive integers nums and a positive integer target, return 
# the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        ans = float('inf')
        for right in range(len(nums)):
            curr += nums[right]
            while curr > target:
                ans = min(ans,right - left +1)
                curr -= nums[left]
                left +=1
            
            if curr == target:
                ans = min(ans,right - left +1)
        if ans == float('inf'):
            return 0
        return ans
            
###Solution
# Sliding window problem.
# Initialize it. Set out ans we will return to inf so that we could find the minimum
# Then we loop through the array and add the first number in the list to curr
# Then we check if the curr is greater than the target:
#     if it is then we take account of the length of that subarray, subtract the previous element in the sub
#     then increment the left by one

# If the target is equals to the target then we just take account the len of the subarray
# We check if the ans == to inf, if yes then we return zero 
# And if not, then we return the min(ans) that we could find.