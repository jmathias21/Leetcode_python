from collections import deque
from typing import List

# https://leetcode.com/problems/buildings-with-an-ocean-view
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 12:22
    def findBuildings(self, heights: List[int]) -> List[int]:
        output = deque()
        max_height = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                output.appendleft(i)
                max_height = heights[i]
        return output

        
solution = Solution()
answer = solution.findBuildings([4,2,3,1])
print(answer)