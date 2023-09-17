from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/subtree-of-another-tree/
# Tags: serialize tree, DFS, recursion
class Solution:

    # Runtime Complexity: O(m + n)
    # Space Complexity: O(m + n)
    # Time: 27:00
    #
    # Serialize both root and subRoot trees and then check to see if the
    # serialized subRoot tree is a substring of serialized root 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serializeTree(root: Optional[TreeNode]):
            if (root is None):
                return 'N'
            
            s1 = serializeTree(root.left)
            s2 = serializeTree(root.right)

            return ''.join([',', str(root.val), s1, s2])
        
        serialized_root = serializeTree(root)
        serialized_subroot = serializeTree(subRoot)

        return serialized_subroot in serialized_root


        
solution = Solution()
answer = solution.isSubtree(TreeNode(12), TreeNode(2))
answer = solution.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2)))
print(answer)