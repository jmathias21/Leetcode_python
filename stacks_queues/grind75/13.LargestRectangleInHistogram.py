from itertools import chain
from typing import List

# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Tags: Stack
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [(0, -1)]
        
        for i, bar in enumerate(chain(heights, [0])):
            while bar < stack[-1][0]:
                # the lowest height is always the last popped stack element
                rect_height = stack.pop()[0]
                rect_left = stack[-1][1]
                max_area = max(max_area, rect_height * (i - rect_left - 1))

            stack.append((bar, i))

        return max_area
        
solution = Solution()
answer = solution.largestRectangleArea([2,1,5,6,2,3])
print(answer)