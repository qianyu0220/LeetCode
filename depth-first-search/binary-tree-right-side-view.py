# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # queue = deque([root])
        # output = []
        # if not root:
        #     return []

        # while queue:
        #     n = len(queue)
        #     for i in range(n):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         if i == n-1:
        #             output.append(node.val)
        # return output
        output = []
        queue = deque([root])
        if not root:
            return []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == n-1:
                    output.append(node.val)
        return output
