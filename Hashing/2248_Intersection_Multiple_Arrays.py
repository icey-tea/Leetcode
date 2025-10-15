# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
# return the list of integers that are present in each array of nums sorted in ascending order.


from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1

        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)
    

# Create a defaultdict to store all the values of the in the 2d array
# Then we are going to loop through the array and increment each intance of the number by 1
# Then at the end all do is loop through our hash and check if the any number appears the same amount of times 
#     as the len of the arr and just append it