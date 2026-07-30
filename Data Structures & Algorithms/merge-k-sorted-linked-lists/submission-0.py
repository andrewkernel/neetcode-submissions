# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = [] 

        for index in lists:
            curr = index

            while curr:
                res.append(curr.val)
                curr = curr.next
            
        res.sort()
        
        dummy = ListNode()
        curr = dummy

        for i in res:
            curr.next = ListNode(i)
            curr = curr.next
        
        return dummy.next

        