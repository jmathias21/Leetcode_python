from typing import List

# https://leetcode.com/problems/find-the-duplicate-number/
# Tags: Floyds Cycle Detection, Fast/Slow Pointer
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = slow

        # iterate slow and fast pointer until they collide (indicating a loop)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
            
        fast = nums[0]

        # P = X, where P is the distance from the first node to the start of the cycle,
        # and X is the distance from the slow/fast intersection to the start of the cycle.
        # So we increment them both until they are equal, and that gives us the beginning
        # of the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

        
solution = Solution()
answer = solution.findDuplicate([1,2,3,4,5,6,7,6])
answer = solution.findDuplicate([2,4,6,1,3,1,5])
answer = solution.findDuplicate([1,3,4,2,2])
print(answer)