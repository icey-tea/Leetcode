# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#My code
class Solution:
    def isValid(self, s: str) -> bool:
        openin = ['(', '{', '[']
        
        stack = []
        for i in s:
            if i in openin:
                stack.append(i)
            elif not stack:
                return False
            else:
                char = stack.pop()
                if i == ')' and char == '(':
                    continue 
                elif i == '}' and char == '{':
                    continue
                elif i == ']' and char == '[':
                    continue
                else:
                    return False
        if stack:
            return False
        return True
    
# Uses a stack for implementation
# Loops throught list of words and of they are an open bracket it appends them to the stack
#     but if it is a closed, it pops  the top item in the stack and check if its  the pair
#         if yes then it pops then it continues
#         if not then it returns False

# The code also handles edge cases.



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for brace in s:
            if brace in brackets:
                if stack and stack[-1] == brackets[brace]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brace)

        return not stack
        

###Better code makes use of a dictionary and uses the key value pairs to work through it 

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        brackets = {'(':')', '[': ']', '{': '}'}
        for char in s:
            if char in brackets:
                stack.append(char)
            elif char not in brackets and stack:
                check = stack.pop()
                if brackets[check] != char:
                    return False
                else:
                    continue
            else:
                return False

        if stack:
            return False
        return True