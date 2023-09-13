from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/balanced-binary-tree/
# Tags: BST, Binary Tree, DFS, recursion
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    #
    # Recurse through the tree with DFS using a post-order recursive
    # function. As we visit each node, return the maximum amount of depth
    # for that node, including the depth of its left and right subtrees.
    # If at anytime we see a difference in depths greater than 1 between
    # the two subtrees, we know that the tree is not height balanced
    def isBalancedRecursive(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root) != -1
        
    def rec(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0

        l_depth = self.rec(root.left)
        r_depth = self.rec(root.right)

        # return -1 if we find out tree is unbalanced, or if we already know
        # its unbalanced
        if (abs(l_depth - r_depth) > 1 or l_depth == -1 or r_depth == - 1):
            return -1
        
        return max(l_depth, r_depth) + 1


        
solution = Solution()
answer = solution.isBalanced(TreeNode(1, None, TreeNode(2, None, TreeNode(3))))
answer = solution.isBalanced(None)
answer = solution.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
answer = solution.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)))
print(answer)