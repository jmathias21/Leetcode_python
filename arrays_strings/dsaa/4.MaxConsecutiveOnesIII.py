from typing import List

# https://leetcode.com/problems/max-consecutive-ones-iii/editorial/
# Tags: Sliding Window
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    #
    # This solution works by using a contracting/expanding window
    # that moves over the array. As we expand the window, we track
    # the reamining flips we have left, and when we exceed our amount
    # we contract the window until we have no longer exceeded the amount
    # left
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxOnes = 0
        remainingFlips = k
        left = 0

        for right in range(0, n):
            # reduce available flips if the next number in the array is a 0
            if (nums[right] == 0):
                remainingFlips -= 1

            # if we have exceeded the number of allowed flips, shrink the window
            # from the left
            while (remainingFlips < 0):
                if (nums[left] == 0):
                    remainingFlips += 1
                left += 1

            # get the maximum concurrent ones by getting the current
            # window size
            maxOnes = max(maxOnes, (right - left) + 1)

        return maxOnes


solution = Solution()
answer = solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
print(answer)

# Example: [0,0,1,0,0,1,1] k = 2
# [[0],0,1,0,0,1,1] remainingFlips = 1, maxOnes = 1
# [[0,0],1,0,0,1,1] remainingFlips = 0, maxOnes = 2
# [[0,0,1],0,0,1,1] remainingFlips = 0, maxOnes = 3
# [0,[0,1,0],0,1,1] remainingFlips = 0, maxOnes = 3
# [0,0,[1,0,0],1,1] remainingFlips = 0, maxOnes = 3
# [0,0,[1,0,0,1],1] remainingFlips = 0, maxOnes = 4
# [0,0,[1,0,0,1,1]] remainingFlips = 0, maxOnes = 5