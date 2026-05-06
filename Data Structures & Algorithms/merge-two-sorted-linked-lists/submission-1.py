# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr = list1
        curr2 = list2

        while curr is not None:
            res.append(curr.val)
            curr = curr.next

        while curr2 is not None:
            res.append(curr2.val)
            curr2 = curr2.next

        
        if not res:
            return None

        res.sort()

        head = ListNode(res[0])
        finalCurr = head

        for i in range(1, len(res)):
            nxt = ListNode(res[i])
            finalCurr.next = nxt
            finalCurr = nxt
        
        return head