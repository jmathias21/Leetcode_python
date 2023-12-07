from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/boundary-of-binary-tree/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 6:04
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs_pre(node):
            if node is None:
                return
            
            if not node.left and not node.right:
                return
            
            output.append(node.val)
            
            if node.left:
                dfs_pre(node.left)
            elif node.right:
                dfs_pre(node.right)

        def dfs_leaf(node):
            if node is None:
                return
            
            if not node.left and not node.right:
                output.append(node.val)
            
            dfs_leaf(node.left)
            dfs_leaf(node.right)

        def dfs_post(node):
            if node is None:
                return
            
            if not node.left and not node.right:
                return
            
            if node.right:
                dfs_post(node.right)
            elif node.left:
                dfs_post(node.left)

            output.append(node.val)

        output.append(root.val)
        if root.left:
            dfs_pre(root.left)
        if root.left or root.right:
            dfs_leaf(root)
        if root.right:
            dfs_post(root.right)
        return output

        
solution = Solution()
answer = solution.boundaryOfBinaryTree(TreeNode(1, TreeNode(1)))
answer = solution.boundaryOfBinaryTree(TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4))))
answer = solution.boundaryOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6, TreeNode(9), TreeNode(10)))))
print(answer)