#Question
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges 
# between them.



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.max = max(self.max, left + right)
            return 1 + max(left, right)
            
        dfs(root)
        return self.max
    
#Solution
# Using Dfs we traverse the tree, as we move up the tree, we search for the max
#     diameter by adding the left and the right side (the heirght of the tree so far).
# Then we return the height of the tree to the node above it so that we can make use 
#     of that height to calculate the the new max diameter