# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 
# If there are duplicates in arr, count them separately.

class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for x in arr:
            if x + 1 in hash_set:
                count += 1
        return count
    
#Use Hashset
#First create a set of the arr
# and the magic behind this is that we have to loop through the original arr and use the hashset to check if
# the value is inside the set. If it is then we return the just increment the count
# and at the end we return the count.