###Question
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the 
# maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = avg = ans = 0 
        for i in range(k):
            curr += nums[i]   
        avg = curr / k
        ans = avg  
        for i in range(k , len(nums)):
            curr += nums[i] - nums[i-k]
            avg  = curr / k
            ans = max(ans, avg) 
        return ans
###Solution
# Use a sliding window
# find thr average for the first k elements
# then you equate that to the max
# next you move the window up by one and subtract the last element (slide the window)
# then you find the average and compare it to the max until you find the max