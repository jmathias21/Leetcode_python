from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 5:32
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1

        return max_depth

        
solution = Solution()
answer = solution.maxDepth("(1+(2*3)+((8)/4))+1")
print(answer)