from typing import List

# https://leetcode.com/problems/generate-parentheses/
# Tags: 
class Solution:

    # Runtime Complexity: O(4^n / sqrt(n)) - Catalan Number
    # Space Complexity: O()
    # Time: started 2:42
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(curr, open, closed):
            if open == 0 and closed == 0:
                output.append("".join(curr))
                return

            if open > 0:
                curr.append('(')
                backtrack(curr, open - 1, closed)
                curr.pop()

            if closed > open:
                curr.append(')')
                backtrack(curr, open, closed - 1)
                curr.pop()

        backtrack([], n, n)
        return output


        
solution = Solution()
answer = solution.generateParenthesis(3)
print(answer)