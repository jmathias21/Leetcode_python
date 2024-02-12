from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def removeInvalidParentheses(self, s: str) -> List[str]:

        open = 0
        to_remove = 0
        for char in s:
            if char == '(':
                open += 1
            elif char == ')':
                if open > 0:
                    open -= 1
                else:
                    to_remove += 1

        def backtrack(curr, i, open, to_remove):
            if i >= len(s):
                return
            
            curr.append(s[i])
            backtrack(curr, i + 1)
            curr.pop()
            if to_remove > 0 and s[i] == ')':
                backtrack(curr, i + 1)




        
solution = Solution()
answer = solution.removeInvalidParentheses("()())()")
print(answer)