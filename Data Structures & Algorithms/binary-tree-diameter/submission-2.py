class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def findHeight(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            left = findHeight(root.left)
            right = findHeight(root.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)
        
        findHeight(root)
        return self.max_diameter