from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 7:00
    def singleNumber(self, nums: List[int]) -> int:
        # 2 + 3 + 4 = 9
        # 9 * 2 = 18
        # 18 - sum(n) = 2
        unique_sum = set()
        for num in nums:
            unique_sum.add(num)

        return (sum(unique_sum) * 2) - sum(nums)

        
solution = Solution()
answer = solution.functionName()
print(answer)