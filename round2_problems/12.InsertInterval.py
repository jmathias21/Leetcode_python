from typing import List
import bisect

# Tags:
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 16:00
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        intervals.insert(bisect.bisect_left([interval[0] for interval in intervals], newInterval[0]), newInterval)

        output.append(intervals[0])

        for i in range(1, len(intervals)):
            prev_interval = output[-1]
            if intervals[i][0] <= prev_interval[1]:
                prev_interval[0] = min(prev_interval[0], intervals[i][0])
                prev_interval[1] = max(prev_interval[1], intervals[i][1])
            else:
                output.append(intervals[i])

        return output


        
solution = Solution()
answer = solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
# [[1,2],[3,10],[12,16]]
print(answer)