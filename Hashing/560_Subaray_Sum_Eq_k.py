# Given an array of integers nums and an integer k, return the total number of subarrays whose sum 
# equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]+nums[i])
        count = defaultdict(int)
        count[0] = 1
        for right in range(len(prefix)):
            ans+=count[prefix[right]- k]
            count[prefix[right]] +=1
        return ans


# First, it pre-calculates and stores all the prefix sums (running totals from the start) in a list called prefix.
# For example, a list $[1, 2, 3]$ becomes $[1, 3, 6]$. Second, it iterates through this prefix list, using a 
# dictionary (count) to track how often each running total has appeared, starting with $\{0: 1\}$. 
# For every current running total (current\_sum), it checks the dictionary for how many times the value 
#  current\_sum - k has appeared. This count is added to the answer because 
#    any segment starting where current\_sum - k occurred and ending now must sum 
# to $\mathbf{k}$. Finally, the current running total's count is updated in the 
# dictionary.