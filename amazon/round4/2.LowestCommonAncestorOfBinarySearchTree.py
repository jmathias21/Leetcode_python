from typing import List

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:23
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return
            
            if (node.val <= p.val and node.val >= q.val) or (node.val <= q.val and node.val >= p.val):
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left if left else right
        
        return dfs(root)


        
solution = Solution()
answer = solution.lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(9))
print(answer)