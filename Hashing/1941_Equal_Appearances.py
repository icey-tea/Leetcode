# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences 
# (i.e., the same frequency).


from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for letter in s:
            count[letter] +=1
        if max(count.values()) != min(count.values()):
            return False
        return True
    
# Just take a record of all the occurences of each item
# and comapare the max value and min Value
# if they are different then just return False