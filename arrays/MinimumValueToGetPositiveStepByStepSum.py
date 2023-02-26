from typing import List

# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/editorial/
# Tags: Prefix Sum
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    #
    # This solution picks a startVal of 1, finds the minimum step by step
    # value, and then sees how close that value is to 1 to get our answer
    # after performing a single loop through nums
    def minStartValue(self, nums: List[int]) -> int:
        startVal = 1
        stepSum = startVal + nums[0]
        minimum = stepSum

        for i in range(1, len(nums)):
            stepSum += nums[i]
            minimum = min(stepSum, minimum)
            
        if minimum < 1:
            return startVal + (1 - minimum)
        else:
            return startVal


solution = Solution()
answer = solution.minStartValue([-3,2,-3,4,2])
print(answer)

# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2

# Input: nums = [1,-2,-3]
# Output: 5
# startValue = 4 | startValue = 5 | nums
#   (4 +1 ) = 5  | (5 +3 ) = 6    |  1
#   (5 -2 ) = 3  | (6 -2 ) = 4    |  -2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3