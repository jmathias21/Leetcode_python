from collections import deque

# https://leetcode.com/problems/maximum-swap/
# Tags: Queue
# Time: 10:00
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val
        if len(self.queue) > self.size:
            popped = self.queue.popleft()
            self.sum -= popped
        return self.sum / len(self.queue)


obj = MovingAverage(3)
param_1 = obj.next(1)
param_1 = obj.next(10)
param_1 = obj.next(3)
param_1 = obj.next(5)