from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/invert-binary-tree/
# Tags: DFS, recursion
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None

        # recursive case
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.right = left
        root.left = right

        return root


        
solution = Solution()
answer = solution.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))))
print(answer)

#          4
#       /     \
#     2         7
#   /   \      /  \
# 1       3  6      9  
#
#          4 <--
#       /     \
#     2         7 <--
#   /   \      /  \
# 1       3  6      9 <--  
# Set TreeNode = 9 left and right to null
#
#          4 <--
#       /     \
#     2         7 <--
#   /   \      /  \
# 1       3  6 <--  9 <--  
# Set TreeNode = 6 left and right to null
#
#          4 <--
#       /     \
#     2         7 <--
#   /   \      /  \
# 1       3  9      6  
# Recurse back up to TreeNode = 7 and flip left and right
#
#          4 <--
#       /     \
#     2         7 <--
#   /   \      /  \
# 1       3  9      6  
# Recurse back up to TreeNode = 4, and flow into left TreeNode
#
# etc.
