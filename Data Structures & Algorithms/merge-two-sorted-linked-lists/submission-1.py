# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list1 and not list2) or (not list1 and not list2):
            return list1
        
        if not list1 and list2:
            return list2

        cur1 = list1
        cur2 = list2
        res = ListNode()
        new = res

        while cur1 and cur2:

            if cur1.val <= cur2.val:
                new.next = cur1
                cur1 = cur1.next
                new = new.next 
            else:
                new.next = cur2
                cur2 = cur2.next
                new = new.next 

        if cur1:
            new.next = cur1
        else:
            new.next = cur2

        return res.next



            


                
        