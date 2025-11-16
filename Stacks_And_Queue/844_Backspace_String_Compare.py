# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.



class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for i in s:
            if stack_s and i == '#':
                stack_s.pop()
            elif i == '#':
                continue
            else:
                stack_s.append(i)
        for j in t:
            if stack_t and j == '#':
                stack_t.pop()
            elif j == '#':
                continue
            else:
                stack_t.append(j)

        return stack_s == stack_t
    
# The general thing we are doing here is creating a stack,
#     then loop throught the words
#     if the stack is not empty and the letter is a #
#         then we remove the last element in the stack
#     if the stack is empty but we have a #   
#         we dont do anything
#     if all else fails:
#         we just append the letter to the stack

# What we do is to then compare the two stacks
