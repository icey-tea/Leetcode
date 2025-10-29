# Given a binary array nums, return the maximum length of a contiguous
# subarray with an equal number of 0 and 1.


from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = ans = 0
        count = {}
        for i,num in enumerate(nums):
            if num == 1:
                prefix += 1
            else:
                prefix -=1
        
            if prefix  == 0:
                ans = i+1
            elif prefix in count:
                ans = max(ans , i - count[prefix])
            else:
                count[prefix] = i
        return ans
            
#For this we use prefix sum and a hash map to find the ans
# to find the longest subarray with equal 0s and 1s, treat 0 as -1 and keep a running prefix sum. each time the prefix is 0, 
# it means all elements up to that point are balanced, so update the 
# answer to i + 1.

# use a dictionary to store the first index where each prefix value 
# appears. if the same prefix occurs again, the subarray between those 
# indices has an equal number of 0s and 1s, so update the maximum length 
# with i - count[prefix]. if the prefix hasn’t appeared, store it with 
# the current index.

# this approach runs in O(n) time and O(n) space. the main idea: 
# repeating prefix values indicate balanced subarrays between their 
# indices.



                            #####
#                         Solution 2
                            #####

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = ans = 0
        count = {}
        count[0] = -1
        for i,num in enumerate(nums):
            if num == 1:
                prefix += 1
            else:
                prefix -=1

            if prefix in count:
                ans = max(ans , i - count[prefix])
            else:
                count[prefix] = i
        return ans



# to find the longest subarray with equal 0s and 1s, convert each 0 to -1 
# so the problem becomes finding the longest subarray with a sum of 0. 
# keep a running count that increases with 1s and decreases with 0s.

# use a hash map to store the first index where each count appears, 
# starting with {0: -1} to handle subarrays from the start. as you loop, 
# if the current count has been seen, update the maximum length using
#  i - counter_mp[count]; otherwise, store the index.


# the algorithm runs in O(n) time and O(n) space. the key idea: when the
# same count repeats, the subarray between those points has 
# equal 0s and 1s.
        