from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:14
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)

        def backtrack(curr, i):
            if i >= n:
                answer.append(curr.copy())
                return

            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            backtrack(curr, i + 1)

        backtrack([], 0)
        return answer

        
solution = Solution()
answer = solution.subsets([1,2,3])
print(answer)