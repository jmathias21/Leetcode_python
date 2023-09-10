from typing import List

# https://leetcode.com/problems/running-sum-of-1d-array/editorial/
# Tags: Prefix Sum
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    #
    # Loop through the set of numbers, summing them
    # on each iteration and replacing the numbers in the
    # list
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        return nums

solution = Solution()
answer = solution.runningSum([1,2,3,4])
print(answer)

# Example: [1,2,3,4]
# [1,2,3,4]
#  ^
# [1,3,3,4]
#    ^
# [1,3,6,4]
#      ^
# [1,3,6,10]
#        ^