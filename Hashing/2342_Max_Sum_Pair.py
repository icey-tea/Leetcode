# You are given a 0-indexed array nums consisting of positive integers. 
# You can choose two indices i and j, such that i != j, and the sum of 
# digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over
# all possible indices i and j that satisfy the conditions. If no such pair
# of indices exists, return -1.

from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        count = defaultdict(int)
        for i, num in enumerate(nums):
            add = 0
            for digit in str(num):
                add += int(digit)

            if add in count:
                ans = max(ans, num + count[add] )
            count[add] = max(count[add],num)
        return ans
    
This is fine but there is a better way of finding the sum of all the
    nums

def getDigitSum(n: int) -> int:
    sumD = 0
    while n > 0:
        sumD += n % 10
        n //= 10
    return sumD

# What this does is finds the modulus(%) 10 of the number 
#     which should give you the last number, in the digit and adds it it
#     to the sum
# then it finds the floor division of the number
#     so as to remove the last number.