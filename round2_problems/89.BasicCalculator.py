from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:52
    def calculate2(self, s: str) -> int:
        s = s.replace(' ', '') + "+"
        str = deque(s)

        def rec():
            total = 0
            curr_num = 0
            operator = "+"
            while str:
                char = str.popleft()
                if char.isdigit():
                    curr_num *= 10
                    curr_num += int(char)
                else:
                    if char == "(":
                        curr_num = rec()
                    if operator == "+":
                        total += curr_num
                    if operator == "-":
                        total -= curr_num
                    if char in ["+", "-"]:
                        operator = char
                    if char == ")":
                        return total
                    curr_num = 0
            return total
                    
        return rec()
    
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '') + "+"
        str = deque(s)

        total = 0
        curr_num = 0
        operator = "+"

        while str:
            char = str.popleft()

            

        
solution = Solution()
answer = solution.calculate("(1+(4+5+2)-3)+(6+8)")
answer = solution.calculate("52 + 64")
print(answer)

# 52 + 64 + (8 - 7)
# ((45 + 2) / 5)