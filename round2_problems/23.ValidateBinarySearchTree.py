from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: 20:00
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, should_be_smaller_than, should_be_greater_than):
            if node is None:
                return True

            if node.val >= should_be_smaller_than or node.val <= should_be_greater_than:
                return False

            left = dfs(node.left, node.val, should_be_greater_than)
            right = dfs(node.right, should_be_smaller_than, node.val)

            return left and right
        
        is_valid_bst = dfs(root, float('inf'), float('-inf'))
        return is_valid_bst
    
solution = Solution()
#answer = solution.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
answer = solution.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
print(answer)