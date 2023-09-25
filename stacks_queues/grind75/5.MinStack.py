# https://leetcode.com/problems/min-stack/
# Tags: stack, stack implementation, tuples

# Time: 30:00
#
# This solution stores the current minimum directly next to each value on
# the stack. When we push a new value onto the stack, we calculate the new
# new minimum and store it next to that value. When we want to get the current
# minimum, we simply look at the minimum stored next to the next value on the
# stack
class MinStackUsingStackOfMinValPairs:

    def __init__(self):
        self.stack = []

    # Runtime Complexity: O(1)
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def pop(self) -> None:
        self.stack.pop()

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def top(self) -> int:
        return self.stack[-1][0]

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def getMin(self) -> int:
        return self.stack[-1][1]

# Time: Not timed
# 
# This solution uses less memory by using a separate min stack that only stores
# the next lowest value and ignores values that are increasing
class MinStackUsingTwoStacks:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def top(self) -> int:
        return self.stack[-1]

    # Runtime Complexity: O(1)
    # Space Complexity: O(n)
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStackUsingTwoStacks()
obj.push(3)
obj.push(3)
obj.pop()
obj.push(4)
obj.push(5)
param_3 = obj.top()
param_4 = obj.getMin()