from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))

            nonlocal max_sum
            max_sum = max(max_sum, left_sum + right_sum + node.val)

            # Path can't split, so pick larger one
            return max(left_sum, right_sum) + node.val

        dfs(root)
        return max_sum


        
solution = Solution()
answer = solution.maxPathSum(TreeNode(2, TreeNode(-1)))
answer = solution.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)