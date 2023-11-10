from typing import List

# https://leetcode.com/problems/trapping-rain-water
# Tags: Stack
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def trap(self, height: List[int]) -> int:
        stack = []
        total_trapped = 0

        for i, bar in enumerate(height):
            while stack and bar > height[stack[-1]]:
                top = stack.pop()

                if not stack:  # No left boundary to trap water
                    break

                distance = i - stack[-1] - 1
                bounded_height = min(bar, height[stack[-1]]) - height[top]
                total_trapped += distance * bounded_height

            stack.append(i)

        return total_trapped

        
solution = Solution()
answer = solution.trap([2,0,0,1,2,3])
answer = solution.trap([3,2,1,0,0,2])
answer = solution.trap([2,0,0,2])
answer = solution.trap([0,0,0,2,1,0,5,0,1,2,3,2,1,0,0,3,2,0,1,0,4,3,0,2,2])
answer = solution.trap([0,1,0,2,1,0,0,3,2,1,2,1])
print(answer)