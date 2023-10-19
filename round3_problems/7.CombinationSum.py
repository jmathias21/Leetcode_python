from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(N^(T/M + 1))
    # Space Complexity: O(T/M)
    # Time: 9:00
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def backtrack(curr, i):
            s = sum(curr)
            if i > len(candidates) - 1:
                return False
            elif s > target:
                return True
            elif s == target:
                answer.append(curr.copy())
                return True

            curr.append(candidates[i])
            sum_too_high = backtrack(curr, i)
            curr.pop()
            if not sum_too_high:
                backtrack(curr, i + 1)

        backtrack([], 0)
        return answer



        
solution = Solution()
#answer = solution.combinationSum([8,7,4,3], 11)
answer = solution.combinationSum([2,3,6,7], 7)
print(answer)