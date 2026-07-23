# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
    
        def dfs(root, maxVal):
            if not root:
                return 0

            goodNodeCount = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)

            goodNodeCount += dfs(root.left, maxVal)
            goodNodeCount += dfs(root.right, maxVal)
            return goodNodeCount
        
        return dfs(root, -101)
