from typing import List

# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [(0, -1)]
        max_area = 0

        for i, height in enumerate(heights):
            while height < stack[-1][0]:
                p_height, p_index = stack.pop()
                left_index = stack[-1][1]
                area = p_height * (i - left_index - 1)
                max_area = max(max_area, area)

            stack.append((height, i))

        return max_area
            
        
solution = Solution()
answer = solution.largestRectangleArea([2,1,2])
answer = solution.largestRectangleArea([2,1,5,6,2,3])
print(answer)