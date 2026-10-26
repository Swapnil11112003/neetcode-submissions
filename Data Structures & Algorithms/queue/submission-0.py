class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True

        return False
        
    def append(self, value: int) -> None:
        new = ListNode(value)
        prev = self.tail.prev
        next = self.tail
        prev.next = new
        new.prev = prev
        new.next = next
        next.prev = new
        

    def appendleft(self, value: int) -> None:
        new = ListNode(value)
        prev = self.head
        next = self.head.next
        prev.next = new
        new.prev = prev
        new.next = next
        next.prev = new

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        cur = self.tail.prev
        next = self.tail
        next.prev = cur.prev
        cur.prev.next = next

        return cur.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        cur = self.head
        next = self.head.next
        next.next.prev = cur
        cur.next = next.next

        return next.val
        
