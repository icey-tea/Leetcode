# Given an array of integers nums and an integer k. A continuous subarray is called nice 
# if there are k odd numbers on it.

# Return the number of nice sub-arrays.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        left = ans = mid = 0
        for right in range(len(nums)):
            if nums[right] %2 != 0:
                odd +=1
                
            while odd > k:
                if nums[left] %2 != 0:
                    odd -=1
                left+=1
                mid = left

            if odd == k:
                while nums[mid] %2 == 0:
                    mid+=1
                ans += (mid - left) +1
                
        return ans
    

# It uses a sliding window approach with three pointers, left, mid and right, to move through the array. 
# The variable odd tracks how many odd numbers are in the current window. 
# When the count of odd numbers exceeds k, the left pointer moves forward to shrink the window until the count 
#     drops back to k. 
# When there are exactly k odd numbers, another pointer mid moves rightward to count how many even numbers can be
#     added to the start of the window without changing the odd count—each of these combinations forms a valid 
#     subarray. The total count of such subarrays is accumulated in ans and returned at the end.
