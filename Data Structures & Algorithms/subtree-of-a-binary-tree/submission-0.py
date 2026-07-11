class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSubtree(root, subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                return (checkSubtree(root.right, subroot.right) and checkSubtree(root.left, subroot.left))
            else:
                return False

        if not subRoot:
            return True
        if not root:
            return False
            
        if root.val == subRoot.val:
            if checkSubtree(root, subRoot):
                return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)