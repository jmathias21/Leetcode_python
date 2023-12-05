from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/range-sum-of-bst/
# Tags: DFS, BST
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 25:00
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0
        def dfs(node):
            if node is None:
                return

            if node.val >= low and node.val <= high:
                nonlocal s
                s += node.val

            if node.val >= low:
                dfs(node.left)
            if node.val <= high:
                dfs(node.right)
        dfs(root)
        return s

        
solution = Solution()
answer = solution.rangeSumBST(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15)
print(answer)