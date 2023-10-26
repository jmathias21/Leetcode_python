from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/path-sum-iii/
# Tags: Prefix sum, DFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 12:00
    #
    # Use prefix sum hash map that gets passed alone recursively. Check to see if current sum - target is in map.
    # If it is, add to our total
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        total = 0
        p = defaultdict(int)
        p[0] = 1

        def dfs(node, s, prefix):
            if node is None:
                return
            
            s += node.val

            if s - targetSum in prefix:
                nonlocal total
                total += prefix[s - targetSum]

            prefix[s] += 1
            dfs(node.left, s, prefix)
            dfs(node.right, s, prefix)
            prefix[s] -= 1

        dfs(root, 0, p)
        return total
        
solution = Solution()
answer = solution.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3, TreeNode(-2))), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), 8)
print(answer)