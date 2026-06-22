# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        count = {}
        index = 0
        while head:
            if head not in count:
                count[head] = 1
            else:
                count[head] += 1

            if count[head] > 1:
                return True
                
            head = head.next

        return False

