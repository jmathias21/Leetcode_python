from typing import List, Optional
from collections import deque, defaultdict

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
    # Time: started 11:06
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None

        dict = defaultdict(list)
        minimum_col = maximum_col = 0

        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is None:
                continue

            minimum_col = min(minimum_col, col)
            maximum_col = max(maximum_col, col)

            dict[col].append(node.val)

            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))

        output = []
        for i in range(minimum_col, maximum_col + 1):
            output.append(dict[i])

        return output

        
solution = Solution()
answer = solution.verticalOrder(TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, None, TreeNode(2))), TreeNode(8, TreeNode(1, TreeNode(5)), TreeNode(7))))
answer = solution.verticalOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)