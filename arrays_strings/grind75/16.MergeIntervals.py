from typing import List

# https://leetcode.com/problems/merge-intervals/
# Tags: intersecting intervals
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    #
    # Sort intervals by the first interval value, then iteratively add them to
    # a merged list. If we see that the last interval added to the merge list
    # overlaps the current interval, we merge them together in the merged list
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []
        for interval in intervals:
            # make sure the merged list is empty or there is in overlap between
            # the last merged interval and the current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            # merge the current interval with the last merged interval
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        return merged

        
        
solution = Solution()
answer = solution.merge([[1,3],[2,6],[8,10],[15,18]])
print(answer)

# Example: [[1,3],[2,6],[8,10],[15,18]]

# merged = []
# merged = [[1,3]] 
# merged = [[1,6]]
# merged = [[1,6],[8,10]]
# merged = [[1,6],[8,10],[15,18]]