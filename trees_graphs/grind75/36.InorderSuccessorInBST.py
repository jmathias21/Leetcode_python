from typing import Optional

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# https://leetcode.com/problems/inorder-successor-in-bst/
# Tags: in-order traversal, DFS
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 45:00
    #
    # Perform in-order DFS. When the value of the node is greater than p, return
    # that as the successor
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None
            
            successor = dfs(node.left)

            if not successor and node.val > p.val:
                return node

            if successor is None:
                successor = dfs(node.right)

            return successor
        
        return dfs(root)


        
solution = Solution()
answer = solution.inorderSuccessor(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), TreeNode(1))
answer = solution.inorderSuccessor(TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4, None, TreeNode(2))), TreeNode(6)), TreeNode(4))
answer = solution.inorderSuccessor(TreeNode(2, TreeNode(1, TreeNode(3))), TreeNode(1))
answer = solution.inorderSuccessor(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), TreeNode(3))
answer = solution.inorderSuccessor(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), TreeNode(6))
print(answer)