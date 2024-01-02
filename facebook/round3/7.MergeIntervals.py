from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O()
    # Time: started 1:03
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result
        
solution = Solution()
answer = solution.merge([[1,3],[2,6],[8,10],[15,18]])
print(answer)