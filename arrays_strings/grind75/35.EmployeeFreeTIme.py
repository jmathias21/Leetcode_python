class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

# https://leetcode.com/problems/employee-free-time/
# Tags: Intervals
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O(n)
    # Time: 25:00
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        output = []
        intervals = sorted([interval for employee in schedule for interval in employee], key=lambda x: x.start)

        largest_end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start > largest_end:
                output.append(Interval(largest_end, intervals[i].start))
            largest_end = max(largest_end, intervals[i].end)

        return output

        
solution = Solution()
answer = solution.employeeFreeTime([[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]])
print(answer)