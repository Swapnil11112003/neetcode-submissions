# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        point = head
        while point:
            length += 1
            point = point.next

        node_from_front = length - n 

        if node_from_front == 0:
            return head.next

        curr = head
        while curr:
            node_from_front -= 1
            if node_from_front == 0:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head


        