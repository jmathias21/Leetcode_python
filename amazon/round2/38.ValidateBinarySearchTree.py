from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: started 1:19
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if node is None:
                return True
            
            if node.val >= low or node.val <= high:
                return False

            left = dfs(node.left, node.val, high)
            right = dfs(node.right, low, node.val)

            if left and right:
                return True
            else:
                return False

        return dfs(root, float('inf'), float('-inf'))
    
solution = Solution()
answer = solution.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
answer = solution.isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))))
answer = solution.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
print(answer)