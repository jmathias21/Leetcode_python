import bisect
from collections import deque

# https://leetcode.com/problems/design-hit-counter/
# Tags: Queue

# Time Complexity: O(n)
# Space Complexity: O(n)
# Time: 30:00
class HitCounter:

    def __init__(self):
        self.queue = deque()
        

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        count = 0
        i = bisect.bisect_right(self.queue, timestamp) - 1
        while i >= 0 and self.queue[i] > timestamp - 300:
            count += 1
            i -= 1

        return count


obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
p1 = obj.getHits(4)
obj.hit(300)
p2 = obj.getHits(300)
p3 = obj.getHits(301)
