###Question
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 
# 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist 
# in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and 
# ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        new = [letter for letter in word] 
        i=j=0
        while j<len(new):
            if new[j] != ch:
                j+=1
            else:
                while i<j:
                    new[i], new[j] = new[j], new[i]
                    i+=1
                    j-=1
                return ''.join(new)
        return ''.join(new)
    
###Solution
# Turn string into a list of letters
# Then initialize  a two pointer with both starting from 0
# Then we make sure we arent exceeding the list while we are looping
# We check if the letter at j of the list is the ch
#     if it is not then we increment j by one
#     else
#         we reverse the sequence of the letters within the range of i and j
#         and at the end we return the list as a string using .join 