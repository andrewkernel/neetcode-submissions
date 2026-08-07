# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        curr1 = list1
        curr2 = list2

        while curr1:
            res.append(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            res.append(curr2.val)
            curr2 = curr2.next

        if len(res) == 0:
            return None
            
        res.sort()
        dummy = ListNode(res[0])
        curr = dummy


        for i in range(1, len(res)):
            nxt = ListNode(res[i])
            curr.next = nxt
            curr = nxt
        return dummy
