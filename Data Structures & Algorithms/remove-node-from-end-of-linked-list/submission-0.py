# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        i, l, r = 0, dummy, head
        while i < n:
            r = r.next
            i += 1
        while r:
            l, r = l.next, r.next
        l.next = l.next.next
        
        return dummy.next
            