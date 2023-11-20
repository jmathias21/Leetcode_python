from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Tags: Post-Order Traversal, DFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            # if a node value is less than 0, we don't want it part of our path
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            nonlocal maximum
            maximum = max(maximum, left + right + node.val)

            return max(left, right) + node.val
        
        dfs(root)
        return maximum

        
solution = Solution()
answer = solution.maxPathSum(TreeNode(2, TreeNode(-1)))
answer = solution.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)