from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:46
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        maximums = []

        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        maximums.append(queue[0])

        for i in range(k, len(nums)):
            if queue and queue[0] == nums[i - k]:
                queue.popleft()

            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            maximums.append(queue[0])

        return maximums

        
solution = Solution()
answer = solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
print(answer)