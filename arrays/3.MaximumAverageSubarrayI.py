from typing import List

# https://leetcode.com/problems/maximum-average-subarray-i
# Tags: Sliding Window
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    #
    # This solution uses a sliding window to determine the maximum average. it also
    # uses a rolling average rather than re-computing the average from scratch every time.
    # In other words, as the window slides, we subtract off the exiting number from the
    # total and we tack on the new number that slid into the window
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s = 0

        # sum the initial window
        for i in range(k):
            s += nums[i]

        # get the max average from the initial sum
        maxAvg = s / k

        for i in range(k, n):
            # tweak the sum based on the shifting of the window
            # rather than re-summing the entire window
            s += nums[i] - nums[i - k]

            maxAvg = max(maxAvg, s / k)

        return maxAvg



solution = Solution()
answer = solution.findMaxAverage([4,2,1,3,3], 2)
answer = solution.findMaxAverage([1,12,-5,-6,50,3], 4)
print(answer)