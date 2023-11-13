from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Time: started 3:17
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        widths = {}

        def dfs(node, n, depth):
            if node is None:
                return
            
            if depth not in widths:
                widths[depth] = (float('inf'), float('-inf'))

            widths[depth] = (min(widths[depth][0], n), max(widths[depth][1], n))
            
            dfs(node.left, 2 * n + 1, depth + 1)
            dfs(node.right, 2 * n + 2, depth + 1)

        dfs(root, 0, 0)
        highest = 0
        for width in widths.values():
            highest = max(highest, width[1] - width[0])
        return highest + 1


solution = Solution()
answer = solution.widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))))
print(answer)