# You are given an array of integers nums, there is a sliding window of size k which is 
# moving from the very left of the array to the very right. You can only see the k numbers in 
# the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        
        ans = []
        for i, num in enumerate(nums):
            if not queue:
                queue.append([i, num])

            while queue and queue[0][0] < i-k+1:
                queue.popleft()

            while queue and num > queue[-1][-1]:
                queue.pop()
            
            queue.append([i, num])

            if i >= k-1:
                ans.append(queue[0][-1])

        return ans

###Monotonically decreasing deque
