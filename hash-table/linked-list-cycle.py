# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpoint = head
        fastpoint = head
        while fastpoint and fastpoint.next:
            slowpoint = slowpoint.next
            fastpoint = fastpoint.next.next
            if slowpoint == fastpoint:
                return True
        return False