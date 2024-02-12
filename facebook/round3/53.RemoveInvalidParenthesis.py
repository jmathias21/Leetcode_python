from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(2 ^ N)
    # Space Complexity: O(N)
    # Time: started 8:56
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l_removed = r_removed = 0

        for char in s:
            if char == ')':
                if l_removed > 0:
                    l_removed -= 1
                else:
                    r_removed += 1
            elif char == '(':
                l_removed += 1

        result = set()
        def backtrack(curr, i, diff, l_to_rem, r_to_rem):
            if l_to_rem == 0 and r_to_rem == 0 and diff == 0 and i == len(s):
                result.add("".join(curr))
                return
            
            if i >= len(s):
                return

            new_diff = diff + 1 if s[i] == '(' else diff - 1 if s[i] == ')' else diff
            if new_diff >= 0:
                curr.append(s[i])
                backtrack(curr, i + 1, new_diff, l_to_rem, r_to_rem)
                curr.pop()

            # only skip if we have parens we want to try removing
            if not s[i].isalpha():
                if l_to_rem > 0 and s[i] == '(':
                    backtrack(curr, i + 1, diff, l_to_rem - 1, r_to_rem)
                if r_to_rem > 0 and s[i] == ')':
                    backtrack(curr, i + 1, diff, l_to_rem, r_to_rem - 1)

        backtrack([], 0, 0, l_removed, r_removed)
        return result


        
solution = Solution()
answer = solution.removeInvalidParentheses("(a)())()")
answer = solution.removeInvalidParentheses("()())()")
print(answer)