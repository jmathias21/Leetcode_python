from typing import List

# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/editorial/
# Tags: Prefix Sum
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    #
    # Loop through each number, and find the minimum
    # sum from all iterations. We can simply take this
    # number and subtract it from 1 to get the minimum
    # positive startVal such that the step by step sum
    # is never less than 1
    def minStartValue(self, nums: List[int]) -> int:
        stepSum = 0
        minimum = 0

        for i in range(0, len(nums)):
            stepSum += nums[i]
            minimum = min(minimum, stepSum)

        return 1 - minimum


solution = Solution()
answer = solution.minStartValue([-3,2,-3,4,2])
print(answer)

# Example: [-3,2,-3,4,2]
# startVal = 0, stepSum = 0, minimum = 0
#
# (0  + -3) = -3
# (-3 +  2) = -1
# (-1 + -3) = -4
# (-4 +  4) =  0
# (0  +  2) =  2
#
# minimum = -4
# startVal = 0
#
# minimum positive value = 1 - minimum
#   = 1 - (-4)
#   = 5
