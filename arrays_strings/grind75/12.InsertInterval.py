from typing import List

# https://leetcode.com/problems/insert-interval/
# Tags: binary search, intersecting intervals
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # binary search
        left = 0
        right = len(intervals) - 1

        # perform binary search to find where to insert the newInterval
        while (left <= right):
            mid = (left + right) // 2
            if (intervals[mid][0] < newInterval[0]):
                left = mid + 1
            else:
                right = mid - 1
        position = left

        # insert the newInterval into the interval list
        intervals.insert(position, newInterval)

        answer = []
        for interval in intervals:
            # if the previous interval does not intersect the current
            # interval, then simply add the current interval to our
            # answer list
            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
            # otherwise, merge the intervals together
            else:
                answer[-1] = [answer[-1][0], max(answer[-1][1], interval[1])]

        return answer

        
solution = Solution()
answer = solution.insert([],[5,7])
answer = solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) # [[1,2],[3,10],[12,16]]
answer = solution.insert([[1,3],[6,9]],[2,5])
print(answer)

# Example: [[1,2],[3,5],[6,7],[8,10],[12,16], [4,8]]
#
# 1. Perform binary search on first element from each interval
# [1, 3, 6, 8, 12], target = 4
# Returned position = 2
#
# 2. Insert newInterval at position in interval
# [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
#
# 3. Build answer by looping through intervals
#
#   answer is empty, append first interval
#   answer = [[1, 2]]
#
#   previous answer interval [1, 2] does not intersect [3, 5]. Append to answer
#   answer = [[1, 2], [3, 5]]
#
#   previous answer interval [3, 5] intersects [4, 8]. Merge them
#   answer = [[1, 5], [3, 8]]

#   previous answer interval [3, 8] inersects [6, 7]. Merge them
#   answer = [[1, 5], [3, 8]]

#   previous answer interval [3, 10] intersects [8, 10]. Merge them
#   answer = [[1, 5], [3, 10]]

#   previous answer interval [3, 10] does not intersect [3, 10]. Append to answer
#   answer = [[1, 5], [3, 10], [12, 16]]