# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        pre, curr = head, head.next
        head.next = None
        while curr != None:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre
