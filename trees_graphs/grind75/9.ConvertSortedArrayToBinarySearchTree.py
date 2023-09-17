from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Tags: BST, Pre-order traversal, DFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(log n) based on height of balanced binary tree
    # Time: Not timed
    #
    # This method uses a recursive operation to build out a new tree
    # using two pointers. It's similar to a binary search, except we're
    # not explicitly looking for a target, but rather continually finding
    # the middle of two moving pointers that are halving the number set
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            # this is a pre-order traversal, meaning we visit the node,
            # then traverse the subtrees. In this case, we set the node
            # to a new TreeNode, then traverse into its branches, where
            # we will start setting those nodes
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


        
solution = Solution()
answer = solution.sortedArrayToBST([1, 2, 3, 4])
answer = solution.sortedArrayToBST([0, 1, 2, 3, 4, 5])
answer = solution.sortedArrayToBST([1])
print(answer)

# Example: [1, 2, 3, 4, 5]
#
# helper(nums, 0, 4) [mid = 3 -> nums[3] = 3]
# |
# |-- helper(nums, 0, 1) [mid = 1 -> nums[1] = 2] 
# |   |
# |   |-- helper(nums, 0, 0) [mid = 0 -> nums[0] = 1]
# |   |
# |   `-- helper(nums, 2, 1)    [No more elements to the left of '2']
# |
# |-- helper(nums, 3, 4) [mid = 4 -> nums[4] = 5]
#     |
#     |-- helper(nums, 3, 3) [mid = 3 -> nums[3] = 4]
#     |
#     `-- helper(nums, 5, 4)    [No more elements to the right of '5']