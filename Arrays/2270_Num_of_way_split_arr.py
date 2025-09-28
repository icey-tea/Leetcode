###Question
# You are given a 0-indexed integer array nums of length n.

# nums contains a valid split at index i if the following are true:

# The sum of the first i + 1 elements is greater than or equal to the sum of the
# last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        curr = 0
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        for i in range(len(nums)-1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                curr +=1
        return curr
    
### Better way to optimize this to O(1) space complexity

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans

#Write solution