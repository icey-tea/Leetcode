###Question
# Given an array nums. We define a running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        return prefix
    
###Solution
#Prefix sum. Thats literally all you need to do