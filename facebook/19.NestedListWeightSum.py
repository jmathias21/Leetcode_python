from typing import List

# https://leetcode.com/problems/nested-list-weight-sum/
# Tags: DFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 30:00
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0

        def dfs(nested_list, depth):
            for n in nested_list:
                if n.isInteger():
                    nonlocal total
                    total += n.getInteger() * depth
                else:
                    dfs(n.getList(), depth + 1)

        dfs(nestedList, 1)
        return total

        
solution = Solution()
answer = solution.depthSum([1,[4,[6]]])
print(answer)