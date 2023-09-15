from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/same-tree/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 11:30
    #
    # Recursively traverse through both trees and build up two ordered arrays
    # based on the traversal order. Then simply compare the arrays
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traverse both trees
        # output array from both trees
        # compare arrays
        arr1 = []
        arr2 = []
        self.getTreeArrayRec(p, arr1)
        self.getTreeArrayRec(q, arr2)
        return arr1 == arr2

    def getTreeArrayRec(self, root: Optional[TreeNode], arr):
        if (root is None):
            arr.append(None)
            return
        else:
            arr.append(root.val)

        self.getTreeArrayRec(root.left, arr)
        self.getTreeArrayRec(root.right, arr)

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Iteratively traverse the two trees by using two stacks to keep track of the next nodes
    # to visit. If at any point the nodes or the corresponding values don't match, then
    # the trees are not the same
    def isSameTreeIterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            q = stack1.pop()
            p = stack2.pop()

            # we XOR the two nodes to see if one is true and one is false. If so,
            # this indicates that the trees are mismatched. Additionally, we check
            # to see if both Nodes are set but the values are mismatched
            if bool(p) ^ bool(q) or (p and q and p.val != q.val):
                return False

            # at this point, we can assume both nodes are both set or are both None,
            # so we can just verify if one of them is set, and add their subtrees to
            # the stack
            if (p):
                stack1.append(p.left)
                stack1.append(p.right)
                stack2.append(q.left)
                stack2.append(q.right)
            
        return True
        
solution = Solution()
answer = solution.isSameTreeIterative(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
answer = solution.isSameTreeIterative(TreeNode(0, TreeNode(-5)),TreeNode(0, TreeNode(-8)))
answer = solution.isSameTreeIterative(TreeNode(1), None)
answer = solution.isSameTreeIterative(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
print(answer)