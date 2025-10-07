###Question
# Given an array of integers nums and an integer target, return indices of the two numbers such that 
# they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:
                return [dic[complement], i]
            dic[num] = i

###Solution
# Use a hashmap to store the each number in nums and its indices
# So we create the hashmap
# Then we loop throught the list of nums. 
#     Her we then find out what number needs to be added to the current number we are on to get the target.
#     And we check if the number needed is already within the hashmap
#     if yes we return the index of what is needed and what we are currently on 
#         but if no we add the number and its index to the hashmap.

# The reason this is better is because checking if a key, value in a hashmap is O(1) but in arrays chcking
# will be O(n)