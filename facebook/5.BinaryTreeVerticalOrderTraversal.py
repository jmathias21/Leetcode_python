from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-vertical-order-traversal
# Tags: BFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 20:00
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = [[] for _ in range(202)]

        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is None:
                continue

            columns[col + 100].append(node.val)

            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))

        return [col for col in columns if col]

        
solution = Solution()
answer = solution.verticalOrder(TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, TreeNode(5))), TreeNode(8, TreeNode(1, None, TreeNode(2)), TreeNode(7))))
answer = solution.verticalOrder(TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7))))
print(answer)