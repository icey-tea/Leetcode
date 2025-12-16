# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding 
# up all the values along the path equals targetSum.

# A leaf is a node with no children.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False

            curr += node.val

            if not node.left and not node.right:
                return curr == targetSum

            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right
        return dfs(root, 0)
    
# Solution

# So we are going to need a helper function here.
# What we are going to be doing is going down the tree and recording the value of 
# each node from the root. 
# When we reach a leaf node, we check if the total from the root till that node is
#     equals to the target and return true or false.

# After working on the left or right leaf node, we compare and return either True or False
# If there was ever a valid path, we will just be retunring True after every Recursion