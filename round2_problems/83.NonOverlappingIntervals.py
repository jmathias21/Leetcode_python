from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O(1)
    # Time: Not timed

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        erased = 0
        k = float('-inf')

        for interval in intervals:
            if interval[0] >= k:
                k = interval[1]
            else:
                erased += 1

        return erased

        
solution = Solution()
answer = solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
print(answer)