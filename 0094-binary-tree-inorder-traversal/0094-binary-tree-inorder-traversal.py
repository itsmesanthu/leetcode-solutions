# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive
        a=[]
        def inorder(node):
            if node is None:
                return None
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
        inorder(root)
        return a
        # s=[]
        # a=[]
        # c=root
        # while c or s:
        #     while c:
        #         s.append(c)
        #         c=c.left
        #     c=s.pop()
        #     a.append(c.val)
        #     c=c.right
        # return a