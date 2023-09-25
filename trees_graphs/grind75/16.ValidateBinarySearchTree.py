from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/validate-binary-search-tree/
# Tags: BST, Valid BST, BST Traversal, BST in-order traversal
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 40:00
    #
    # As we drill down into the left and right nodes, we continuously narrow
    # down the bounds. If any node breaks these bounds, we return False
    def isValidBSTUsingBoundsRec(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root, float('inf'), float('-inf'))

    def rec(self, node: Optional[TreeNode], should_be_less_than, should_be_greater_than):
        if node is None:
            return True
        
        if node.val >= should_be_less_than:
            return False
        
        if node.val <= should_be_greater_than:
            return False
        
        if (not self.rec(node.left, node.val, should_be_greater_than) or
            not self.rec(node.right, should_be_less_than, node.val)):
            return False

        return True
    
    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    #
    # This uses an in-order recursive traversal of the BST. If at any point during
    # that traversal the current value is smaller or equal to the previous value,
    # then we know its not a valid BST
    def isValidBSTUsingInOrderTraversalRec(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        return self.inOrderTraversalRec(root)


    def inOrderTraversalRec(self, node):
        if node is None:
            return True

        if not self.inOrderTraversalRec(node.left):
            return False

        if node.val <= self.prev:
            return False
        
        self.prev = node.val

        return self.inOrderTraversalRec(node.right)
    
    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    #
    # This uses an in-order iterative traversal of the BST. If at any point during
    # that traversal the current value is smaller or equal to the previous value,
    # then we know its not a valid BST
    def isValidBSTUsingInOrderTraversalIterative(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        stack = [root]
        while stack:
            n = stack[-1]

            if n.left:
                stack.append(n.left)
                n.left = None
                continue

            if n.val <= prev:
                return False
            
            prev = n.val

            stack.pop()
            
            if n.right:
                stack.append(n.right)

        return True

        
solution = Solution()
answer = solution.isValidBSTUsingInOrderTraversalIterative(TreeNode(2, TreeNode(1), TreeNode(3)))
answer = solution.isValidBST(TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6))))
answer = solution.isValidBSTUsingInOrderTraversalIterative(TreeNode(5, TreeNode(4), TreeNode(7, TreeNode(6), TreeNode(10, TreeNode(9)))))
answer = solution.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
print(answer)