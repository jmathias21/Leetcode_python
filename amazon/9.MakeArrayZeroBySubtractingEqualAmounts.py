from typing import List

# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
# Tags: Hash Set
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 10:00
    def minimumOperations(self, nums: List[int]) -> int:
        # get unique number count, excluding 0
        unique_nums = set()

        for num in nums:
            if num > 0:
                unique_nums.add(num)

        return len(unique_nums)

        
solution = Solution()
answer = solution.minimumOperations([1,5,0,3,5])
print(answer)