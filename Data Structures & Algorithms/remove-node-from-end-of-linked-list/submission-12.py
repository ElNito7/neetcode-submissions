# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None
        end, temp = head, head
        pre = head
        count, l = 0, 1
        while end.next:
            end = end.next 
            l += 1
        while count < l-n:
            pre = temp
            temp = temp.next
            count += 1
        if l-n == 0:
            head = head.next
        else:
            pre.next = temp.next
            temp.next = None
        return head