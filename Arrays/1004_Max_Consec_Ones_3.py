###Question
# # Given a binary array nums and an integer k, return the maximum number of consecutive 
# # 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = curr = count = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                curr += 1
            elif nums[right] != 1 and count <= k:
                curr +=1
                count +=1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                    left+=1
                    curr-=1
                else:
                    curr -=1
                    left+=1
            ans = max(ans , curr)

        return ans
    
###Solution
# So the way i went about this was to for initalize my slidinig window 
# Then if the number we were on was a one, i would add 1 to the curr
# But if the number is a 0 and the counter which records the amount of ones if less
#     than k:
#     i would increment counter and also curr
# But if counter is greater than k:
#     Subtract the last number in the list until the counter is equals to k while 
#     also reducing curr by 1
# and continue noramlly 