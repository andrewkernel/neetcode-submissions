# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        N = 0
        while cur:
            N += 1
            cur = cur.next
        
        removeIndex = N - n

        if removeIndex == 0:
            return head.next 

        cur = head

        for i in range(removeIndex - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head


