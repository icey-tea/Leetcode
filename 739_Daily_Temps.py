# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to 
# wait after the ith day to get a warmer temperature. If there is no future day for 
# which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans  = [0] * len(temperatures)
        stack = []
        for i , temp in enumerate(temperatures):
            while stack and temp > stack[-1][-1]:
                remIndex, remTemp  = stack.pop()
                val = i - remIndex
                ans[remIndex] = val
            stack.append([i,temp])
        return ans
    
