class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    #
    # While traversing the tree, if p and q nodes are both to the right,
    # of the current node, then we keep traversing the tree to the right.
    # Same for if they are both to the left. When we see that p and q nodes
    # split, then we know we've found our lowest common ancestor (LCD).
    #
    # Note: If the current node is equal to p or q, then we know it must
    # be the LCD, because a node can be a descendant of itself, and we
    # know its the lowest node that has both p and q as descendants.
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        

        
solution = Solution()
#answer = solution.lowestCommonAncestor(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), TreeNode(2), TreeNode(3))
answer = solution.lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(4))
#answer = solution.lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(7))
print(answer)