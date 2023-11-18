from typing import List
import heapq

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:20
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        meeting_rooms = []

        for i in range(len(intervals)):
            if meeting_rooms and intervals[i][0] >= meeting_rooms[0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, intervals[i][1])

        return len(meeting_rooms)

    
        
solution = Solution()
answer = solution.minMeetingRooms([[0,30],[5,10],[15,20]])
print(answer)