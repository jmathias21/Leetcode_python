from typing import List
import heapq

# https://leetcode.com/problems/meeting-rooms-ii
# Tags: Min heap, prioity queue
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Sort the intervals by the start times. Now we know the following:
    #   1. If the start time of a new meeting is before the end time of all existing meetings, then we need another meeting room
    #   2. If the start time of a new meeting is after the the end time of the next meeting to end, we can use their meeting room
    # Based on these two observations, we can opt to use a min heap to track the next meeting to end and determine if we need
    # to free up a new room or if we can use an existing room.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_rooms = []
        intervals.sort(key=lambda x: (x[0]))

        for i in range(len(intervals)):
            if meeting_rooms and intervals[i][0] >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, intervals[i][1])

        return len(meeting_rooms)


        
solution = Solution()
answer = solution.minMeetingRooms([[5,15],[6,20],[9,18],[8,11],[13,17],[1,19]])
answer = solution.minMeetingRooms([[13,15],[1,13]])
answer = solution.minMeetingRooms([[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]])
answer = solution.minMeetingRooms([[1,10],[1,7],[1,3],[4,7],[8,9]])
answer = solution.minMeetingRooms([[0,30],[5,10],[15,20]])
print(answer)