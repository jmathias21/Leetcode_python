from collections import deque
from typing import List

# https://leetcode.com/problems/basic-calculator-ii/
# Tags: Stack
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def calculate(self, s: str) -> int:
        curr_num = 0
        operator = '+'
        stack = []

        s = s.replace(' ', '')
        s += "+" # ensure the last digit is added back to the stack

        for char in s:
            if char.isdigit():
                curr_num = (curr_num * 10) + int(char)
            else:
                if operator == '+':
                    stack.append(curr_num)
                if operator == '-':
                    stack.append(-curr_num)
                if operator == '*':
                    stack.append(stack.pop() * curr_num)
                if operator == '/':
                    operant = stack.pop()
                    stack.append((abs(operant) // curr_num) * (-1 if operant < 0 else 1))
                operator = char
                curr_num = 0

        return sum(stack)
        
solution = Solution()
answer = solution.calculate("14 - 3 / 2")
answer = solution.calculate("3 + 2 * 2 / 4")
print(answer)