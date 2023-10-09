from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:32
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None

            l_node = dfs(node.left)
            r_node = dfs(node.right)

            if node.val == p.val or node.val == q.val:
                return node
            
            if l_node and r_node:
                return node

            return l_node if l_node else r_node
        
        test = dfs(root)
        return test



        
solution = Solution()
TreeNode
answer = solution.lowestCommonAncestor(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), TreeNode(5), TreeNode(0))
print(answer)