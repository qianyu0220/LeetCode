# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        point1 = headA
        point2 = headB
        while point1!=point2:
            point1 = point1.next if point1 else headB 
            point2 = point2.next if point2 else headA
        return point1
