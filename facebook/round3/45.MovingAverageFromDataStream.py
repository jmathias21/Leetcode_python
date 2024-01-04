from collections import deque
from typing import List

# 
# Tags: 
class MovingAverage:

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    # Time: 
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0
        

    def next(self, val: int) -> float:
        self.window.append(val)
        self.window_sum += val

        if len(self.window) > self.size:
            popped = self.window.popleft()
            self.window_sum -= popped

        return self.window_sum / len(self.window)

        
solution = MovingAverage(3)
answer = solution.next(1)
answer = solution.next(10)
answer = solution.next(3)
answer = solution.next(5)
print(answer)