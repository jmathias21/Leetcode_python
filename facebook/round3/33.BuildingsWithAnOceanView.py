from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 11:03
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        result = deque()

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                result.appendleft(i)
                max_height = heights[i]

        return result

        
solution = Solution()
answer = solution.findBuildings([4,2,3,1])
print(answer)