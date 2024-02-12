from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        output = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append((char, len(output)))
                output.append(char)
            elif char == ')':
                if stack:
                    output.append(char)
                    stack.pop()
            else:
                output.append(char)

        while stack:
            _, i = stack.pop()
            output[i] = ""

        return "".join(output)


        
solution = Solution()
answer = solution.minRemoveToMakeValid("(a(b(c)d)")
answer = solution.minRemoveToMakeValid("lee(t(c)o)de)")
print(answer)