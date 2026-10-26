class ListNode():
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        cur = self.head.next
        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1

        if cur == self.tail or index != 0:
            return -1

        return cur.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        next = self.head.next
        prev = self.head
        prev.next = new
        new.prev = prev
        new.next = next
        next.prev= new

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        next = self.tail
        prev = self.tail.prev
        prev.next = new
        new.prev = prev
        new.next = next
        next.prev = new
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return 

        cur = self.head.next
    
        while cur and index > 0:
            index -= 1
            cur = cur.next

        if cur is None:
            return

        new = ListNode(val)
        prev = cur.prev
        prev.next = new
        new.prev = prev
        new.next = cur
        cur.prev = new
          

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        i = 0
        while cur != self.tail:
            if i == index:
                next = cur.next
                prev = cur.prev
                prev.next = next
                next.prev =  prev
                return

            i += 1
            cur = cur.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)