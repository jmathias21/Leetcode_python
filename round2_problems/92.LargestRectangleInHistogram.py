from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:53
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, -1)]
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            height = heights[i]

            while stack[-1][0] > height:
                popped_height, _ = stack.pop()

                rect_left = stack[-1][1]

                max_area = max(max_area, popped_height * (i - rect_left - 1))

            stack.append((height, i))

        return max_area
        
solution = Solution()
answer = solution.largestRectangleArea([2,1,2])
answer = solution.largestRectangleArea([2,1,5,6,2,3])
print(answer)