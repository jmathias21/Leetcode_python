from typing import List

# https://leetcode.com/problems/subsets/
# Tags: Backtracking, DFS, recursion
class Solution:

    # Runtime Complexity: O(n * 2 ^ n)
    # Space Complexity: O(n)
    # Time: 55:00
    #
    # Uses DFS backtracking with recursion to generate a decision tree. At each node,
    # we decide either to add the next number onto the current array, or skip that number.
    # When we reach the maximum height of the tree by exhausting all numbers, we add the
    # current array to our answer array
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(curr, i):
            if i >= len(nums):
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

# Example: [1,2,3]
#
#                   /                    \ 
#                 [1]                     []
#            /           \            /       \
#          [1,2]        [1]         [2]       []
#        /       \      /    \     /   \     /   \
#    [1,2,3]  [1,2] [1,3]    [1] [2,3]  [2] [3]  []
#
# At each node of the tree, we have two options:
# 1. Grab the next number
# 2. Skip the next number