import heapq
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        meeting_rooms = [intervals[0][1]]

        for i in range(1, len(intervals)):
            # if the meeting we want to book occurs before the next meeting to end, we need a new room
            if intervals[i][0] >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, intervals[i][1])

        return len(meeting_rooms)

        
solution = Solution()
answer = solution.minMeetingRooms([[9,10],[4,9],[4,17]])
print(answer)