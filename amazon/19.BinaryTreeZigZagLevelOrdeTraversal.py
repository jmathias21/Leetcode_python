from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()

            if node is None:
                continue

            if depth >= len(output):
                output.append([])

            if depth % 2 == 0:
                output[depth] = output[depth] + [node.val]
            else:
                output[depth] = [node.val] + output[depth]

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return output

        

        
solution = Solution()
answer = solution.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)