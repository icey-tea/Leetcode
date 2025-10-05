###Question
# Given a string s, reverse the order of characters in each word within a sentence while still preserving 
#     whitespace and initial word order.


class Solution:
    def reverseWords(self, s: str) -> str:
        new = s.split(' ')
        ans = []
        for item in new:
            ans.append(item[::-1])
        return ' '.join(ans)
    

###Solution
# Split the string into a list that contain each word within the string
# Then loop through each word and reverse the string 
# lastly just append the reversed string and join it all together using .join()