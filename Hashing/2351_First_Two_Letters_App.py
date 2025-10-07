# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Note:

# A letter a appears twice before another letter b if the second occurrence of a is before the 
# second occurrence of b.
# s will contain at least one letter that appears twice.


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                return s[i]
            dic[s[i]] = i

# Use a hashmap
# Here we just loop throught the string and check if the letter is already in the dic
# if yes then we just return the letter,
# else we just add the new letter and its index to the dic