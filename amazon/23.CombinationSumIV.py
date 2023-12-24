from typing import List

# https://leetcode.com/problems/combination-sum-iv/
# Tags: 
class Solution:

    # Runtime Complexity: O(T * N)
    # Space Complexity: O(T)
    # Time: started 1:42
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(sum):
            if sum > target:
                return 0
            
            if sum in memo:
                return memo[sum]
            
            if sum == target:
                return 1
                
            total = 0
            for num in nums:
                total += dfs(sum + num)

            memo[sum] = total
            return total


        test = dfs(0)
        return test


        
solution = Solution()
answer = solution.combinationSum4([1,2,3], 4)
print(answer)