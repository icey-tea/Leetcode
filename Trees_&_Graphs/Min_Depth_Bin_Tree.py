class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left and right:  
            return (1+ min(left, right))
        
        if not left and not right:
            return 1
        
        return 1 + (left if left else right)