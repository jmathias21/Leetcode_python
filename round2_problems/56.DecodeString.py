from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 45:00
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr_str = deque()
                while stack[-1] != "[":
                    c = stack.pop()
                    curr_str.appendleft(c)

                stack.pop()
                curr_num = deque()
                while stack and stack[-1].isdigit():
                    c = stack.pop()
                    curr_num.appendleft(c)

                stack.append("".join(curr_str * int("".join(curr_num))))

        return "".join(stack)


        
solution = Solution()
answer = solution.decodeString("3[a]2[bc]")
answer = solution.decodeString("3[a2[c]]")
print(answer)