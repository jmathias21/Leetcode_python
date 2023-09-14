from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/diameter-of-binary-tree/
# Tags: binary tree, DFS, tuples
class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 33:00
    #
    # Recurse through the tree. On way back up the stack, keep track of both
    # the current longest left and right diameter subtrees from the current Node,
    # as well as the highest sum of both left and right diameters. The highest sum
    # is the longest diameter
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.rec(root)[1]
    
    def rec(self, root: Optional[TreeNode]) -> (int, int):
        if (root is None):
            return 0, 0

        left_diameter, left_sum = self.rec(root.left)
        right_diameter, right_sum = self.rec(root.right)

        return max(left_diameter, right_diameter) + 1, max(left_sum, right_sum, left_diameter + right_diameter)

        
solution = Solution()
answer = solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(3)), TreeNode(5, TreeNode(4, None, TreeNode(8)), TreeNode(6))), TreeNode(3, None, TreeNode(4))))
print(answer)

#          1
#       /     \
#     2         7
#   /   \         \
# 1       3         9 
#       /
#     4
#
# Recursing back up through the stack:
# LD = left diameter, RD = right diameter, L + R = sum of left and right diameter
# Node 4, LD = 0, RD = 0, L + R = 0
# Node 3, LD = 1, RD = 0, L + R = 1
# Node 1, LD = 0, RD = 0, L + R = 0
# Node 2, LD = 1, RD = 2, L + R = 3
# Node 9, LD = 0, RD = 0, L + R = 0
# Node 7, LD = 0, RD = 1, L + R = 1
# Node 1, LD = 3, RD = 2, L + R = 5
#
# The highest L + R = 6, therefore the longest diameter is 6, which can be visualized
# by drawing a line from Node 4 to Node 9