# Question
# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and 
# backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


def isPalindrome(self, s: str) -> bool:
    import string
    translator = str.maketrans('', '', string.punctuation)
    s = s.translate(translator)
    s = s.lower()
    s = s.replace(' ','')
    left = 0
    right = len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True

### Explanation
# So we import string so that we can use translate to remove all puctuations. 
# The next thing is to turn everything to lowercase and remove all spaces inside the text. 
# The way the pointer works is that it first established, then we check if the left pointer and right pointer are the same.
# If no then we return faslse.
# Else we just increment the pointer until left > right and return True


def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) -1
    while left < right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right-=1
        elif not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1
    return True

###Explanation
# This one removes the need for an import to be used
# The two pointers and initialized 
# We check if the values are alphanums
#     If not then we just move the pointer by one (to the next one) and check again if it an alphanum
# Then we check if the values for the left and right are the same vaule
#     If yes then we check if the lower version of the values are different
#         if yes then we return False
#     If no then we just increment the pointers and check again
# If everythin runs then we return True at the end

