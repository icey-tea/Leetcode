###Question
# Given a string s and an integer k, return the maximum number of vowel letters 
# in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        left = count = ans = 0
        
        for letter in s[0:k]:
            if letter in vowels:
                count+=1
        ans = count
            
        for right in range(k,len(s)):
            if s[left] in vowels:
                count-=1
            if s[right] in vowels:
                count +=1
            left+=1
            ans = max(ans, count)
        return ans
    
###Solution
# Sliding window problem. INitialize
# Start by looping throught the first k elements are storing thr amount of times a vowel appeared.
# After that we loop throught the other elements and take note that :
#     if the last element we removed was a vowel, we reduce the count by one
#     if the element we just added is a vowel then we add one to the count 
#     and then compare the count with the ans to find the max
# Then return the ans

