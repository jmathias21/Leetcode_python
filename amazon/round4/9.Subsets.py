from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(2 ^ n)
    # Space Complexity: O()
    # Time: started 11:37
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(curr, i):
            if i >= len(nums):
                result.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            backtrack(curr, i + 1)

        backtrack([], 0)
        return result

        
solution = Solution()
answer = solution.subsets([1,2,3])
print(answer)