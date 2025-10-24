# Given an integer array nums, return the largest integer that only occurs once. 
# If no integer occurs once, return -1.


from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        ans = -1
        for num in nums:
            hashmap[num] += 1
        for key in hashmap:
            if hashmap[key] == 1:
                ans = max(ans, int(key))
        return ans
        
# Just create a hashmap for the arr
# Then set out ans to -1 and just loop through the hashmap, taking note of values that have a frequency of -1
# changing the ans to the max between the values