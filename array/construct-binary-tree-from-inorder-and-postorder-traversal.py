# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder = deque(postorder)
        def build(inorder):
            if inorder:
                idx = inorder.index(postorder.pop())
                root = TreeNode(inorder[idx])
                root.right = build(inorder[idx+1:])
                root.left = build(inorder[:idx])
                return root
        return build(inorder)