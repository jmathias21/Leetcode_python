from collections import deque
from typing import List

# https://leetcode.com/problems/sliding-window-maximum/
# Tags: Monotonic Decreasing Queue
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(k)
    # Time: Not timed
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        maximums = []

        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        maximums.append(queue[0])

        for i in range(k, len(nums)):
            # make sure we only remove the element if it is existing the window
            if queue and queue[0] == nums[i - k]:
                queue.popleft()

            # remove elements from queue that are smaller than current num, as
            # they will never be candidates for the maximum
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            maximums.append(queue[0])

        return maximums

        
solution = Solution()
answer = solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(answer)