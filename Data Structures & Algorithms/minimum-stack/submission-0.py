class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_list.append(val if len(self.stack) == 1 else min(self.getMin(), val))
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
