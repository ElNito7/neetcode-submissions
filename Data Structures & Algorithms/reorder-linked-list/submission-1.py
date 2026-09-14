# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 
        l1, l2 = head, head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        rev = l1.next
        pre, temp = rev, rev.next
        pre.next = None

        while temp:
            pos = temp.next
            temp.next = pre
            pre = temp
            temp = pos
        temp = head
        
        while pre:
            pos = temp.next
            temp.next = pre
            posPre = pre.next
            pre.next = pos
            temp = pos
            pre = posPre
        temp.next = None
