### Question
# Given a 1-indexed array of integers numbers that is already sorted in 
# non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an 
# integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not 
# use the same element twice.

# Your solution must use only constant extra space.

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers)-1 
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        else: 
            if numbers[right] + numbers[left] < target:
                left +=1
            elif numbers[right] + numbers[left] > target:
                right -=1 

###Solution
# First initialze your two poiters
# First we check if the sum of the two values are equals to the target.
# If not:
#     Then we check if the sum is less than the taregt:
#         if yes then we move the left pointer forward
#     if no then we move the right poiter backwards