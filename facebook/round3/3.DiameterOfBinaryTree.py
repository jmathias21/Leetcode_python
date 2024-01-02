from typing import Optional

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node, depth):
            if node is None:
                return depth - 1
            
            l_depth = dfs(node.left, depth + 1)
            r_depth = dfs(node.right, depth + 1)

            nonlocal max_diameter
            max_diameter = max(max_diameter, (l_depth - depth) + (r_depth - depth))

            return max(l_depth, r_depth)

        dfs(root, 0)
        return max_diameter

        
solution = Solution()
answer = solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)))
print(answer)