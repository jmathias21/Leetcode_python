from typing import List

# https://leetcode.com/problems/maximum-subarray/
# Tags: Kadane's Algorithm
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 10:00
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float('-inf')

        for num in nums:
            if curr_sum < 0 and num > curr_sum:
                curr_sum = num
            else:
                curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum

        
solution = Solution()
answer = solution.maxSubArray([-2,-1])
answer = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(answer)