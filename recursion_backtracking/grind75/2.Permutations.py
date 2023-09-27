from typing import List

# https://leetcode.com/problems/permutations/
# Tags: backtracking, DFS, recursion
class Solution:

    # Runtime Complexity: O(n * n!)
    # Space Complexity: O(n)
    # Time: started 2:45
    # 
    # Uses DFS recursive backtracking to traverse a "tree" of potential permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(cur):
            if len(nums) == len(cur):
                answer.append(cur.copy())
                return

            for num in nums:
                if num not in cur:
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()

        backtrack([])
        return answer
            
        
solution = Solution()
answer = solution.permute([1,2,3])
print(answer)

# Example: permute
# nums = [1,2,3]

#         /    |    \
#       [1]   [2]    [3]
#      / |    / \     | \
#    [2][3]  [1][3]  [1][2]
#    /   |    |  |    |   \
#  [3]  [2]  [3] [1] [2]  [1]

# answer = [[1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]]