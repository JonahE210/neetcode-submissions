class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        def levelTraverse(level, root):
            if not root:
                return
            
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)

            levelTraverse(level + 1, root.left)
            levelTraverse(level + 1, root.right)

        if not root:
            return res

        levelTraverse(0, root)
        return res