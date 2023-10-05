from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 12:00
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        # √(x1 - x2)2 + (y1 - y2)2
        for point in points:
            distances.append(((point[0]**2) + point[1]**2, point))

        distances.sort()
        return [dist[1] for dist in distances[:k]]

        
solution = Solution()
answer = solution.kClosest([[1,3],[-2,2]], 1)
print(answer)