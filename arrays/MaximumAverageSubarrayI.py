from typing import List

# https://leetcode.com/problems/maximum-average-subarray-i/editorial/
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
        highestAvg = 0
        total = 0

        for i in range(k):
            total += nums[i]

        highestAvg = total / k

        for i in range(k, n):
            total -= nums[i - k]
            total += nums[i]
            highestAvg = max(highestAvg, total / k)

        return highestAvg


solution = Solution()
answer = solution.findMaxAverage([1,12,-5,-6,50,3], 4)
print(answer)