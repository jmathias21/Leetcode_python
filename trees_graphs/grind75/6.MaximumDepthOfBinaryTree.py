from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Tags: DFS, binary tree, depth
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 1:30
    #
    # When recursing back up the tree we return the max depth
    # between the left and right subtrees and add 1. This yields
    # the maximum depth when we get back to the root
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

        
solution = Solution()
answer = solution.maxDepth()
print(answer)