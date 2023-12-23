from typing import List

# https://leetcode.com/problems/two-sum/
# Tags: Hash Map
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 10:00
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i

        
solution = Solution()
answer = solution.twoSum([2,7,11,15], 9)
print(answer)