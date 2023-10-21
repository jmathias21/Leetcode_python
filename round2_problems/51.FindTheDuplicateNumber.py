from collections import Counter
import heapq
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 15:00
    def findDuplicate2(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        new_nums = [(-freq, num) for num, freq in frequency.items()]
        heapq.heapify(new_nums)
        return heapq.heappop(new_nums)[1]
    
    def findDuplicate(self, nums: List[int]) -> int:
        # p = x, where p is the distance from the starting point to the start of a cycle, and x
        # is the distance from the slow/fast pointers to the cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        
solution = Solution()
answer = solution.findDuplicate([1,3,4,2,2])
print(answer)