class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node,maxNode,minNode):
            if not node:
                return maxNode- minNode
            
            if node.val > maxNode:
                maxNode = node.val
            if node.val < minNode:
                minNode = node.val
            
            left = dfs(node.left,maxNode, minNode)
            right = dfs(node.right, maxNode, minNode)
            
            
            return max(left, right)
            
            
        return (dfs(root, root.val, root.val)) 
            