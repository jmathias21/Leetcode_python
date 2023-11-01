from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 45:00
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        level_min = float('inf')
        level_max = float('-inf')
        queue = deque([(root, 1)])

        while queue:
            new_queue = deque()
            while queue:
                node, val = queue.popleft()

                level_min = min(level_min, val)
                level_max = max(level_max, val)

                if node.left:
                    new_queue.append((node.left, (val * 2) - 1))
                if node.right:
                    new_queue.append((node.right, val * 2))

            max_width = max(max_width, level_max - level_min)
            level_min = float('inf')
            level_max = float('-inf')
            queue = new_queue

        return max_width + 1



        
solution = Solution()
answer = solution.widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, TreeNode(7)))))
print(answer)