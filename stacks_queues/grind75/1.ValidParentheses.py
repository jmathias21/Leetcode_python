# https://leetcode.com/problems/valid-parentheses/
# Tags: stacks
class Solution:
    pMap = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            # Add open brackets to stack
            if c in ['(', '{', '[']:
                stack.append(c)
                continue

            if c in [')', '}', ']']:
                # if stack is empty and we're looking at a closed
                # bracket, it means that there's more closed
                # brackets than open brackets, so we return false
                if len(stack) == 0:
                    return False

                # pop the last open bracket and make sure it matches
                # the current closed bracket. If not, we know we know
                # the order is incorrect
                p = stack.pop()
                if self.pMap.get(c) != p:
                    return False

        # if the stack isn't empty, it means there's more open brackets
        # than closed brackets, so we return false
        return len(stack) == 0

        
solution = Solution()
answer = solution.isValid("{([])}") # valid
print(answer)
answer = solution.isValid("{[}]") # not valid
print(answer)