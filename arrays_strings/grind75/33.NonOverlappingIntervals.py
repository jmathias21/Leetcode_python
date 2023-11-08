from typing import List

# https://leetcode.com/problems/non-overlapping-intervals/
# Tags: Interval Scheduling Problem, Greedy
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # This is an "Interview Scheduling Problem".
    # 1. Sort the intervals by end time
    # 2. Starting with smallest end time, compare it to the next start time
    #   - If next start time is after current end time, erase it
    #   - If next start time is before current end time, set current end time to the next end time
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        k = float('-inf')
        erased_intervals = 0

        for interval in intervals:
            start_time, end_time = interval
            if start_time >= k:
                k = end_time
            else:
                erased_intervals += 1

        return erased_intervals

        
solution = Solution()
answer = solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
answer = solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[1,4]])
print(answer)