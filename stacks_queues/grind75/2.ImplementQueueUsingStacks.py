# https://leetcode.com/problems/implement-queue-using-stacks/
# Tags: Stack, Queue
# Time: 34:40
class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def push(self, x: int) -> None:
        self.stack1.append(x)

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def peek(self) -> int:
        if not self.stack2:
            while (self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    # Runtime Complexity: O(1)
    # Space Complexity: O(1)
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


myQueue = Solution()
myQueue.push(1) # 1
myQueue.push(2) # 1, 2
myQueue.push(3) # 1, 2, 3
myQueue.push(4) # 1, 2, 3, 4
myQueue.pop()   # 2, 3, 4
myQueue.push(5) # 2, 3, 4, 5
myQueue.pop()   # 3, 4, 5
myQueue.pop()   # 4, 5
myQueue.pop()   # 5
myQueue.pop()   #
myQueue.peek()
myQueue.empty()