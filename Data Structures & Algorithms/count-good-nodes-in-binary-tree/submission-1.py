# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        self.goodNodeCount = 0
        path = []
        def dfs(root):
            if not root:
                return
            path.append(root.val)
            maxVal = max(path)

            if path[-1] == maxVal:
                self.goodNodeCount += 1

            dfs(root.left)
            dfs(root.right)
            path.pop()

        if root:   
            dfs(root)
        return self.goodNodeCount
