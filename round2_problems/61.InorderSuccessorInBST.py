from typing import Optional

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
    # Time: started 5:10
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        def dfs(node):
            if node is None:
                return
            
            successor = dfs(node.left)

            if not successor:
                if node.val > p.val:
                    return node
                else:
                    successor = dfs(node.right)

            return successor
        
        return dfs(root)

        
solution = Solution()
answer = solution.inorderSuccessor(TreeNode(2, None, TreeNode(3)), TreeNode(2))
answer = solution.inorderSuccessor(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), TreeNode(2))
print(answer)