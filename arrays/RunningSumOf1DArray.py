from typing import List

# https://leetcode.com/problems/running-sum-of-1d-array/editorial/
# Tags: Prefix Sum
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums

solution = Solution()
answer = solution.runningSum([1,2,3,4])
print(answer)

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].