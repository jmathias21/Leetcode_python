from typing import List

# https://leetcode.com/problems/generate-parentheses/
# Tags: Catalan number, backtracking
class Solution:

    # Runtime Complexity: O((4 ^ n ) / (sqrt(n)): Catalan number approximation
    # Space Complexity: O(n)
    # Time: 18:00
    #
    # Use backtracking. There are two paths at each iteration: Open or Closed. Only append an open paren
    # if we have some left to add and only append a closed paren if closed > open
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(curr, opens, closes):
            if opens == 0 and closes == 0:
                output.append(''.join(curr))
                return
            
            if opens > 0:
                curr.append('(')
                backtrack(curr, opens - 1, closes)
                curr.pop()

            if closes > opens:
                curr.append(')')
                backtrack(curr, opens, closes - 1)
                curr.pop()

        backtrack([], n, n)
        return output

        
solution = Solution()
answer = solution.generateParenthesis(3)
print(answer)