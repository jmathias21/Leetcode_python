from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: started 3:24
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        min_needed = 0

        for char in s:
            if char == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    min_needed += 1

        min_needed += open
        return min_needed


        
solution = Solution()
answer = solution.minAddToMakeValid("))((()()")
answer = solution.minAddToMakeValid("((()()")
print(answer)