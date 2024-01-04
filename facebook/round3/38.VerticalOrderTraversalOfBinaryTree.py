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

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_column = 1000
        max_column = -1000
        column_map = defaultdict(list)
        queue = deque([(root, 0, 0)])

        while queue:
            node, col, depth = queue.popleft()

            if node is None:
                continue

            column_map[col].append((depth, node.val))

            min_column = min(min_column, col)
            max_column = max(max_column, col)

            queue.append((node.left, col - 1, depth + 1))
            queue.append((node.right, col + 1, depth + 1))

        result = []
        for i in range(min_column, max_column + 1):
            column_map[i].sort()
            result.append([n[1] for n in column_map[i]])

        return result

            


        
solution = Solution()
answer = solution.verticalTraversal(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)