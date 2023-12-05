from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Tags: BFS
class Solution:

    # Runtime Complexity: O(n log(n/k))
    # Space Complexity: O(n)
    # Time: 17:00
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        smallest = largest = 0

        queue = deque([(root, 0, 0)])

        while queue:
            node, col, depth = queue.popleft()

            if node is None:
                continue

            smallest = min(smallest, col)
            largest = max(largest, col)
            d[col].append((depth, node.val))

            queue.append((node.left, col - 1, depth + 1))
            queue.append((node.right, col + 1, depth + 1))

        output = []
        for i in range(smallest, largest + 1):
            output.append([item[1] for item in sorted(d[i])])
        return output

        
solution = Solution()
answer = solution.verticalTraversal(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)