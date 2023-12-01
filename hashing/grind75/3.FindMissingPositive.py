from typing import List

# https://leetcode.com/problems/first-missing-positive/
# Tags: Cycle Sort
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # find first missing number
        i = 1
        for num in nums:
            if num != i:
                return i
            i += 1
        return i

        
solution = Solution()
answer = solution.firstMissingPositive([1,2,3,4])
answer = solution.firstMissingPositive([8,7,1,4])
answer = solution.firstMissingPositive([3,4,-1,1])
print(answer)