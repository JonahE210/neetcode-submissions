class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def find_diameter(root):
            if not root:
                return 0

            left = find_diameter(root.left)
            right = find_diameter(root.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        find_diameter(root)
        return self.max_diameter