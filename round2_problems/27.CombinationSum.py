from typing import List

# 
# Tags: 
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target)]
        dp[0] = [[0]]

        for candidate in candidates:
            for i in range(candidate, target + 1):
                for combination in dp[i - candidate]:
                    dp[i].append(combination + [candidate])
                

        return dp[target]

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 5:06
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def backtrack(i, curr, s):
            if s == target:
                answer.append(curr.copy())
                return True
            if s > target or i >= len(candidates):
                return True

            curr.append(candidates[i])
            left = backtrack(i, curr, s + candidates[i])
            curr.pop()
            if not left:
                backtrack(i + 1, curr, s)

            return False

        backtrack(0, [], 0)
        return answer

            

        
solution = Solution()
answer = solution.combinationSum([2,3,6,7], 7)
print(answer)