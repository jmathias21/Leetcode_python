from typing import List
import heapq

# Time: started 9:55
class MedianFinder:

    def __init__(self):
        self.lo = [float('inf')]
        self.hi = [float('inf')]
        

    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            if num <= self.hi[0]:
                heapq.heappush(self.lo, -num)
            else:
                lowest_in_hi = heapq.heappop(self.hi)
                heapq.heappush(self.lo, -lowest_in_hi)
                heapq.heappush(self.hi, num)
        else:
            if num < -self.lo[0]:
                heapq.heappush(self.lo, -num)
                highest_in_lo = -heapq.heappop(self.lo)
                heapq.heappush(self.hi, highest_in_lo)
            else:
                heapq.heappush(self.hi, num)


    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        else:
            return -self.lo[0]
        


obj = MedianFinder()
obj.addNum(5)
obj.addNum(8)
obj.addNum(2)
obj.addNum(1)
obj.addNum(3)
obj.addNum(4)
obj.addNum(9)
p1 = obj.findMedian()