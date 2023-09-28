class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 60:00
    #
    # Perform a recursive DFS of the binary tree to find the LCA by looking for one of the
    # target descendants, and then if found, passing it up the stack
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            
            # if we find one of the target nodes we can short circuit our search.
            # If the other target node is a child node of the target node we found,
            # then it works out because this node becomes the LCA
            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            # if both left and right trees return a node back, it indicates that the
            # current node is the LCA
            if left and right:
                return node
            
            # if only one node is returned from one side, pass that node up the stack
            return left if left is not None else right
            
        return dfs(root)
            

        
solution = Solution()
p_node = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q_node = TreeNode(1, TreeNode(0), TreeNode(8))
root_node = TreeNode(3, p_node, q_node)
answer = solution.lowestCommonAncestor(root_node, p_node, q_node)

p_node = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q_node = p_node.right.right
root_node = TreeNode(3, p_node, TreeNode(1, TreeNode(0), TreeNode(8)))
answer = solution.lowestCommonAncestor(root_node, p_node, q_node)
print(answer)