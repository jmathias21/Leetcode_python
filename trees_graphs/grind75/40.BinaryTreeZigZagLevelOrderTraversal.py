from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Tags: Level-order traversal, BFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O()
    # Time: 21:00
    #
    # Perform level-order BFS traversal. On odd iterations, prepend our output with the current node value
    # rather than adding it to the end
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        output = []

        while queue:
            node, depth = queue.popleft()

            if node is None:
                continue

            if len(output) == depth:
                output.append([])

            if depth % 2 != 0:
                output[depth] = [node.val] + output[depth]
            else:
                output[depth] = output[depth] + [node.val]

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return output


        
solution = Solution()
answer = solution.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5))))
answer = solution.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)