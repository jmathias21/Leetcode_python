from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:58
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr_str = deque()
                curr_digit = deque()
                while stack:
                    char = stack.pop()
                    if char.isalpha():
                        curr_str.appendleft(char)
                    elif char.isdigit():
                        curr_digit.appendleft(char)
                        if not stack or not stack[-1].isdigit():
                            stack.extend(curr_str * int(''.join(curr_digit)))
                            break

        return "".join(stack)

        
solution = Solution()
#answer = solution.decodeString("3[a]2[bc]")
answer = solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
answer = solution.decodeString("2[abc]3[cd]ef")
print(answer)