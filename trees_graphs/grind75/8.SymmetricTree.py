from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/symmetric-tree/
# Tags: recursion, binary tree, DFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 17:30
    #
    # Checks to see if two binary trees are symmetric by traversing
    # the left side using a left-first DFS, and traversing the right side
    # using a right-first DFS, and adding the current node valiue to an array
    # for each side on the way back up the stack. Then we compare the two
    # arrays and verify they are the same
    def isSymmetricUsingRecursion1(self, root: Optional[TreeNode]) -> bool:
        left_arr = self.recLeft(root.left)
        right_arr = self.recRight(root.right)

        return left_arr == right_arr

    def recLeft(self, root: Optional[TreeNode]):
        if root is None:
            return [None]

        arr1 = self.recLeft(root.left)
        arr2 = self.recLeft(root.right)

        return [root.val] + arr1 + arr2
        
    def recRight(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return [None]

        arr1 = self.recRight(root.right)
        arr2 = self.recRight(root.left)

        return [root.val] + arr1 + arr2
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # This method uses recursion to traverse both trees simultaenously,
    # unlike the previous method of traversing the left and right sides
    # separately
    def isSymmetricUsingRecursion2(self, root: Optional[TreeNode]) -> bool:
        return self.isMirrorRec(root.left, root.right)

    def isMirrorRec(self, t1: Optional[TreeNode], t2: Optional[TreeNode]):
        if t1 is None and t2 is None:
            return True
        
        if t1 is None or t2 is None:
            return False

        return (t1.val == t2.val
            and self.isMirrorRec(t1.left, t2.right)
            and self.isMirrorRec(t1.right, t2.left))
    

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Uses a stack to keep track of the next nodes to process. We traverse
    # the left and right trees simulataneously, comparing the values as they
    # are processed
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack1 = [root.left]
        stack2 = [root.right]

        while stack1 and stack2:
            t1 = stack1.pop()
            t2 = stack2.pop()

            if t1 is None and t2 is None:
                continue

            if t1 is None or t2 is None or t1.val != t2.val:
                return False

            stack1.extend([t1.left, t1.right])
            stack2.extend([t2.right, t2.left])

        return True
    


        
solution = Solution()
answer = solution.isSymmetric(TreeNode(1))
answer = solution.isSymmetricIterative(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))))
answer = solution.isSymmetricIterative(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))
print(answer)