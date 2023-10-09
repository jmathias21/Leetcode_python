from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n * n!)
    # Space Complexity: O()
    # Time: started 11:10
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(curr):
            if len(curr) == len(nums):
                answer.append(curr.copy())
                return

            for i, num in enumerate(nums):
                if num in curr:
                    continue
                curr.append(num)
                backtrack(curr)
                curr.pop()

        backtrack([])
        return answer

        
solution = Solution()
answer = solution.permute([1,2,3])
print(answer)