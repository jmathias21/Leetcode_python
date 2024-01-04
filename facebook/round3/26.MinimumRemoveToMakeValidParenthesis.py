from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 8:08
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        output = []

        for i, char, in enumerate(s):
            if char == '(':
                output.append(char)
                stack.append((char, len(output) - 1))
            elif char == ')':
                if stack:
                    stack.pop()
                    output.append(char)
            else:
                output.append(char)

        while stack:
            _, i = stack.pop()
            output[i] = ""

        return "".join(output)


        
solution = Solution()
answer = solution.minRemoveToMakeValid("))((")
answer = solution.minRemoveToMakeValid("lee(t(c)o)de)")
print(answer)