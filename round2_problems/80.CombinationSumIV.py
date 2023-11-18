from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 12:54
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        nums.sort()

        def dfs(sum):
            if sum in memo:
                return memo[sum]

            if sum > target:
                return 0
            
            if sum == target:
                return 1
            
            res = 0
            for i in range(len(nums)):
                if sum + nums[i] <= target:
                    res += dfs(sum + nums[i])
                else:
                    break

            memo[sum] = res
            return memo[sum]

        return dfs(0)

        
solution = Solution()
#answer = solution.combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10)
answer = solution.combinationSum4([1,2,3], 4)
print(answer)