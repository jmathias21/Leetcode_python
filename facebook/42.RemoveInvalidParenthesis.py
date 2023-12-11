from typing import List

# https://leetcode.com/problems/remove-invalid-parentheses/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    def removeInvalidParentheses2(self, s: str) -> List[str]:
        valid_parens = set()

        l_removed, r_removed = 0, 0
        for char in s:
            if char == ')':
                if l_removed > 0:
                    l_removed -= 1
                else:
                    r_removed += 1
            elif char == '(':
                l_removed += 1


        def backtrack(curr, diff, r_rem, i):            
            nonlocal r_removed
            if r_rem > r_removed:
                return

            if curr and i == len(s) and diff == 0:
                valid_parens.add("".join(curr))
                return
            
            if i >= len(s):
                return
            
            new_diff = diff + 1 if s[i] == '(' else diff - 1 if s[i] == ')' else diff

            if new_diff >= 0:
                curr += s[i]
                backtrack(curr, new_diff, r_rem, i + 1)
                curr.pop()

            if not s[i].isalpha():
                backtrack(curr, diff, r_rem + 1 if s[i] == ')' else r_rem, i + 1)

        backtrack([], 0, 0, 0)
        if not valid_parens:
            return [""]
        return valid_parens


        
solution = Solution()
# answer = solution.removeInvalidParentheses("(a)())()")
# answer = solution.removeInvalidParentheses("x(")
# answer = solution.removeInvalidParentheses("(")
answer = solution.removeInvalidParentheses("()())()")
print(answer)