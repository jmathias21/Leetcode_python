from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 8:28
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_order = 100
        max_order = -100
        column_map = defaultdict(list)

        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is None:
                continue

            column_map[col].append(node.val)
            
            min_order = min(min_order, col)
            max_order = max(max_order, col)
            
            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))

        result = []
        for i in range(min_order, max_order + 1):
            result.append(column_map[i])

        return result

        
solution = Solution()
answer = solution.verticalOrder(TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7))))
print(answer)