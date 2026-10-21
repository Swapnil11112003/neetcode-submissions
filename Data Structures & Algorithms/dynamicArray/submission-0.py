class DynamicArray:
    
    def __init__(self, capacity: int):
        self.l = [] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.l[i]

    def set(self, i: int, n: int) -> None:
        self.l[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.getSize():
            self.resize()
        self.l.append(n)

    def popback(self) -> int:
        popped = self.l.pop()
        return popped

    def resize(self) -> None:
        cap = self.capacity
        resized = [] * cap * 2
        for item in self.l:
            resized.append(item)
        self.l = resized
        self.capacity = cap * 2

    def getSize(self) -> int:
        return len(self.l)
        
    def getCapacity(self) -> int:
        return self.capacity
