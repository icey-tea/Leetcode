class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if node == None:
                return 0 
            
            if node.val >= maxVal:
                good = 1
            else:
                good = 0
               
            newMax = max(node.val, maxVal)

            return (good + dfs(node.left,newMax)+ dfs(node.right, newMax))

        return dfs(root, root.val)
    

    