class MedianFinder:

    def __init__(self):
        self.li = []
        

    def addNum(self, num: int) -> None:
        self.li.append(num)
        
    def findMedian(self) -> float:
        self.li.sort()

        if len(self.li) % 2 != 0:
            return self.li[len(self.li)//2]
        else: 
            return (self.li[len(self.li)//2] + self.li[len(self.li)//2 - 1]) / 2

        
        