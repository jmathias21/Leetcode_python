from typing import List, Optional

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 7:45
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        def dfs(node):
            if node is None:
                return
            
            successor = dfs(node.left)
            if successor:
                return successor

            if node.val > p.val:
                return node

            return dfs(node.right)
        
        return dfs(root)

        
solution = Solution()
answer = solution.inorderSuccessor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2))
answer = solution.inorderSuccessor(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), TreeNode(6))
answer = solution.inorderSuccessor(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), TreeNode(1))
print(answer)