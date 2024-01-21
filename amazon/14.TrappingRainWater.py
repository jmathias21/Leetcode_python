from typing import List

# https://leetcode.com/problems/trapping-rain-water/
# Tags: Stack
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped = 0

        for i, bar in enumerate(height):
            while stack and bar > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                bounded_height = min(height[stack[-1]], bar) - height[top]
                trapped += distance * bounded_height
            stack.append(i)

        return trapped  

        
solution = Solution()
answer = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(answer)