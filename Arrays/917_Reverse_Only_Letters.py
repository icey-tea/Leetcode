###Question
# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right  = len(s)-1
        s = [letter for letter in s]
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            elif s[left].isalpha() == False:
                left+=1
            else:
                right-=1
                
        return ''.join(s)

###Solution
# Use two pointers (initialize it)
# Then use list comprehension to change string to a list of the individual characters
# Use the two pointers to check if both characters are letters and switch
# But if they arent you move the pointer by one
