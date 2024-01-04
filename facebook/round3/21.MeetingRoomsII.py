from typing import List
import heapq

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 3:40
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meeting_rooms = []
        intervals.sort(key=lambda x: x[0])
        
        for i in range(len(intervals)):
            # if the current meeting's start time is after the next meeting to end's end time, use
            # their meeting room
            if meeting_rooms and intervals[i][0] >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, intervals[i][1])

        return len(meeting_rooms)




        
solution = Solution()
answer = solution.minMeetingRooms([[0,30],[5,10],[15,20]])
print(answer)