# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left,right)
    
# Solution

# The idea behind this is that each time we call the maxDepth fuction, what we do is 
# move down to the next level (either left or right) until we reach the leaf, 
#     Then we use the base case which will return 0 for the left and right after each 
#     call of the funtion has ran 

# But the main thing is that what we return after we work on each node is going to be 
#     the max between the left and right plus 1 which will serve as the depth or 
#     from what i think the longest number of nodes we have visited 