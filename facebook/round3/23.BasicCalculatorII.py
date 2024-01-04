from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 16:00
    def calculate(self, s: str) -> int:
        s += ('+')
        s = s.replace(' ', '')
        operator = "+"
        stack = []
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num *= 10
                curr_num += int(char)
            else:
                if operator == '*':
                    stack[-1] *= curr_num
                elif operator == '/':
                    sign = -1 if stack[-1] < 0 else 1
                    stack[-1] = (abs(stack[-1]) // curr_num) * sign
                elif operator == '-':
                    stack.append(-curr_num)
                elif operator == '+':
                    stack.append(curr_num)
                operator = char
                curr_num = 0

        return sum(stack)

        
solution = Solution()
answer = solution.calculate("14-3/2")
answer = solution.calculate(" 3+5 / 2 ")
print(answer)