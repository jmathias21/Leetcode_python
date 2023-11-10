import heapq

# https://leetcode.com/problems/find-median-from-data-stream/
# Tags: Heap
# Time: Not timed
class MedianFinder:

    # Space Complexity: O(n)
    def __init__(self):
        self.lo = [] # max heap
        self.hi = [] # min heap
        

    # Time Complexity: O(logn)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        

    # Time Complexity: O(1)
    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) / 2
        else:
            return -self.lo[0]
        

obj = MedianFinder()
obj.addNum(1)
obj.addNum(3)
obj.addNum(3)
obj.addNum(6) # <-- median
obj.addNum(7)
obj.addNum(8)
obj.addNum(9)
p1 = obj.findMedian() # 6

obj = MedianFinder()
obj.addNum(1)
obj.addNum(3)
obj.addNum(4) # <-- median
obj.addNum(5) # <-- median
obj.addNum(6)
obj.addNum(7)
p2 = obj.findMedian() # 4.5