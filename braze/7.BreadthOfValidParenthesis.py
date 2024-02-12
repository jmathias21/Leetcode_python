from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def breadthofValidParenthesis(self, s) -> int:
        if len(s) == 0:
            return 0

        depth = 0
        depth_counts = {}

        for char in s:
            if char == '(':
                depth += 1
            elif depth > 0:
                if depth in depth_counts:
                    depth_counts[depth] += 1
                else:
                    depth_counts[depth] = 1
                depth -= 1

        return max(depth_counts.values())

        
solution = Solution()
# answer = solution.breadthofValidParenthesis(')')
# answer = solution.breadthofValidParenthesis('())')
answer = solution.breadthofValidParenthesis('( () () () ) ()')
print(answer)