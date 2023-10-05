import bisect
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 15:00
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1

        def rec(node, left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(nums[mid])
            node.left = rec(node.left, left, mid - 1)
            node.right = rec(node.right, mid + 1, right)

            return node

            
        root = TreeNode()
        answer = rec(root, left, right)

        return answer


        
        
            


solution = Solution()
answer = solution.sortedArrayToBST([-10,-3,0,5,9])
print(answer)

# [-10,-3,0,5,9]
