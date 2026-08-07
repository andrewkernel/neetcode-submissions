# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        l1 = list1
        l2 = list2

        while l1:
            res.append(l1.val)
            l1 = l1.next
        
        while l2:
            res.append(l2.val)
            l2 = l2.next
        
        if not res:
            return None
        
        res.sort()
        dummy = ListNode(res[0])
        head = dummy

        for i in range(1, len(res)):
            nxt = ListNode(res[i])
            head.next = nxt
            head = nxt
        return dummy