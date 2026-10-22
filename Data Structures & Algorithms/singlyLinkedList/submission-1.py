class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new
        if self.head == self.tail:
            self.tail = new

        
    def insertTail(self, val: int) -> None:
        new = Node(val)
        self.tail.next = new
        self.tail = self.tail.next
        
    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        l = []
        cur = self.head.next
        while cur:
            l.append(cur.val)
            cur = cur.next
        return l
        
