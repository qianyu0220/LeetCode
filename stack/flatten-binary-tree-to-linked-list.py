# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None

            cur = root.right
            while cur.right:
                cur = cur.right
            cur.right = temp
