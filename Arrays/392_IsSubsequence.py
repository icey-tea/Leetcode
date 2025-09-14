###Question
# Given two strings s and t, return true if s is a subsequence of t, or false 
# otherwise.
# A subsequence of a string is a new string that is formed from the 
# original string by deleting some (can be none) of the characters without 
# disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=j=0
        ans = []
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                ans.append(s[i])
                i+=1
                j+=1

            else:
                j+=1
        ans = ''.join(ans)
        if len(s) == len(ans):
            return True
        else:
            return False

###Solution
# Initialize two pointers
# if the value of the pointer in s == to the pointer in t:
#     append to ans
#     move i by one and j by one

# else:
#     move only j by one

# Change ans into a string and then compare with s
# if s == ans then return True
