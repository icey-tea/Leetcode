# Given a string text, you want to use the characters of text to
# form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum
# number of instances that can be formed.



from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        ans = float('inf')
        word = 'ballon'
        if 'l' in count and 'o' in count:
            count['l'] = count['l'] //2
            count['o'] = count['o'] //2
        for letter in word:
            ans = min(ans, count[letter])
        return ans
        
# Count the amount of times each char appears
# set ans to inf
# then we divide the count of 'l' and 'o' by 2
# Loop through the word balloon and just find the min