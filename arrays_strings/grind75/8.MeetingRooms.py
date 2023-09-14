from typing import List

# https://leetcode.com/problems/meeting-rooms/
# Tags: Lambda, Sort
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O()
    # Time: 30:00
    #
    # This solution uses sorting to speed up the performance. We only need to
    # compare the start time of the next meeting to the end time of the previous
    # meeting, and so on
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the outer list using the first element (meeting start) of the inner list
        intervals.sort(key=lambda x: x[0])

        # track the previous meeting end time
        prev_meeting_end = -1

        for meeting in intervals:
            meeting_start = meeting[0]
            meeting_end = meeting[1]

            # if the start of the next meeting is smaller than the end time
            # of the previous meeting, then we know they conflict
            if meeting_start < prev_meeting_end:
                return False
            
            prev_meeting_end = meeting_end
            
        return True

        
solution = Solution()
answer = solution.canAttendMeetings([[1, 2],[8, 9],[4, 5]])
print(answer)