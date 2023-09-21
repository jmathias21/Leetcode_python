from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/3sum/editorial/
# Tags: BFS, level order, binary tree
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 12:30
    #
    # A level order traversal is the same thing as a breadth first search.
    # Meaning this is a BFS implementation. In this case, we use recursion to
    # perform a pre-order traversal of the nodes, and at each depth we build
    # an array of node values for all nodes at that depth
    def levelOrderUsingRecursion(self, root: Optional[TreeNode]) -> List[List[int]]:
        def rec(root: Optional[TreeNode], depth: int,  output: List[List[int]]):
            # check to see if we're at a new depth level in the tree
            # that we haven't encountered before and append an empty array
            # so that we don't get out-of-bounds errors when we add our
            # node values to the array at this depth
            if depth == len(output):
                output.append([])

            output[depth].append(root.val)

            if root.left:
                rec(root.left, depth + 1, output)
            if root.right:    
                rec(root.right, depth + 1, output)

        if not root:
            return []
        
        output = []
        rec(root, 0, output)

        return output
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # We use a stack to keep track of nodes and perform a pre-order traversal.
    # We pass the current depth along in the stack, and use it to build and array
    # of node values for all nodes at that depth
    def levelOrderUsingStack(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        stack = [(root, 0)]

        while stack:
            r, depth = stack.pop()

            if depth == len(output):
                output.append([])

            output[depth].append(r.val)

            if r.right:
                stack.append((r.right, depth + 1))
            if r.left:
                stack.append((r.left, depth + 1))

        return output



        
solution = Solution()
answer = solution.levelOrder()
answer = solution.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
print(answer)

# Example:
#        3 <--
#       / \
#      9   20
#          / \
#         15  7
# Node 3 has depth 0. Add to output:
# [[0]]

#        3
#       / \
#  --> 9   20
#          / \
#         15  7
# Node 9 has depth 1. Add to output:
# [[0], [9]]

#        3
#       / \
#      9   20 <--
#          / \
#         15  7
# Node 20 has depth 1. Add to output:
# [[0], [9,20]]

#        3
#       / \
#      9   20
#          / \
#     --> 15  7
# Node 15 has depth 2. Add to output:
# [[0], [9,20], [15]]

#        3
#       / \
#      9   20
#          / \
#         15  7 <--
# Node 7 has depth 2. Add to output:
# [[0], [9,20], [15,7]]