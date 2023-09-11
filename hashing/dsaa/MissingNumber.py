from typing import List

# https://leetcode.com/problems/missing-number/editorial/
# Tags: Hash Set
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def missingNumber(self, nums: List[int]) -> int:
        n = set(nums)
        for x in range(len(nums) + 1):
            if not x in n:
                return x

solution = Solution()
answer = solution.missingNumber([0,1])
print(answer)

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
#  2 is the missing number in the range since it does not appear in nums.