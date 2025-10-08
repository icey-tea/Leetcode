# Given an array nums containing n distinct numbers in the range [0, n], return the only number 
# in the range that is missing from the array.


###Slower 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        for num in nums:
            if 0 not in nums:
                return 0
            if (num+1) not in nums:
                return num+1
            
# What we do here is change the list to a set so that we can we can perform search operations in O(1)
# Then we sort it so we can loop through it better

# Loop throught the set of numbers and all we do is check if the next number (num +1) is present
#     if not then we return num +1

# but the outliner is if we dont have a zero so we can just return it if the set doesnt have it since it is
# first number that should be in the list




###Fatser Method
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum
    
# The array contains numbers in the range [0, n], but one number is missing.
# If we know the sum of all numbers from0 to n, and subtract the sum of elements present in 
# the array, the result will be the missing number.

# Let n be the length of the array.

# Compute the expected sum of numbers from 0 to n using the formula:
# ExpectedSum=n∗(n+1)/2

# Compute the actual sum of the array elements.

# Subtract actual sum from expected sum → the difference is the missing number.
