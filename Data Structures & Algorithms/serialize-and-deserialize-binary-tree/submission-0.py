# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []
        def traverse(tree, root) -> Optional[List[str]]:
            if not root:
                tree.append("null")
                return
            
            tree.append(str(root.val))
            traverse(tree, root.left)
            traverse(tree, root.right)
            return tree
        
        traverse(res, root)
        string = ",".join(res)
        return string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "null":
                self.index += 1
                return 

            node = TreeNode(int(nodes[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
            
