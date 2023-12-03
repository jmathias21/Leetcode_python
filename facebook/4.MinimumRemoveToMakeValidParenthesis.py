# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 20:00
    #
    # Use stack to track open parens. At thend end, if there's open parens, remove them from
    # the output
    def minRemoveToMakeValid(self, s: str) -> str:
        output = []
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                output.append('(')
                stack.append(('(', len(output) - 1))
            elif char == ')':
                if stack:
                    stack.pop()
                    output.append(')')
            else:
                output.append(char)

        while stack:
            _, i = stack.pop()
            output[i] = ""

        return "".join(output)


        
solution = Solution()
answer = solution.minRemoveToMakeValid("))((")
print(answer)