# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def validNodes(root, left, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False

            return validNodes(root.left, left, root.val) and validNodes(root.right, root.val, right)
        
        return validNodes(root, float("-inf"), float("inf"))

