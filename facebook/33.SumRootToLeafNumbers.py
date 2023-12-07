from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Tags: DFS
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(H)
    # Time: 11:00
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        def dfs(node, sum):
            if node is None:
                return
            
            sum *= 10
            sum += node.val
            
            if not node.left and not node.right:
                nonlocal total_sum
                total_sum += sum
            
            dfs(node.left, sum)
            dfs(node.right, sum)

        dfs(root, 0)
        return total_sum
    
        
solution = Solution()
answer = solution.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)))
print(answer)