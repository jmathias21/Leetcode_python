# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Tags: Stack
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 11:00
    def minAddToMakeValid(self, s: str) -> int:
        total = 0
        stack = []
        for char in s:
            if char  == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    total += 1

        return total + len(stack)

        
solution = Solution()
answer = solution.minAddToMakeValid(")")
answer = solution.minAddToMakeValid("())")
answer = solution.minAddToMakeValid("(()(()(()")
answer = solution.minAddToMakeValid(")))()(((")
print(answer)