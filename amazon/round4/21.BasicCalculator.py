from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def calculate(self, s: str) -> int:
        expr = deque(s.replace(' ', '') + "+")

        def calc():
            s = 0
            curr_num = 0
            operator = '+'

            while expr:
                char = expr.popleft()
                if char.isdigit():
                    curr_num = curr_num * 10 + int(char)
                else:
                    if char == '(':
                        curr_num = calc()
                    if operator == '+':
                        s += curr_num
                    if operator == '-':
                        s -= curr_num
                    
                    if char in ['+','-']:
                        operator = char
                    if char == ')':
                        return s
                    curr_num = 0
            return s

        return calc()

        
solution = Solution()
answer = solution.calculate("1 + 1")
answer = solution.calculate("(1+(4+5+2)-3)+(6+8)")
print(answer)