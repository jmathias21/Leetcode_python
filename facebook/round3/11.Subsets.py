from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n * 2 ^ n)
    # Space Complexity: O()
    # Time: started 1:08
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(curr, i):
            if i >= len(nums):
                output.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            backtrack(curr, i + 1)

        backtrack([], 0)
        return output

        
solution = Solution()
answer = solution.subsets([1,2,3])
print(answer)