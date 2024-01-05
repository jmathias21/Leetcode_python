from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 5:03
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def dfs(node, s):
            if node is None:
                return
            
            s *= 10
            s += node.val

            if not node.left and not node.right:
                nonlocal total_sum
                total_sum += s
            
            dfs(node.left, s)
            dfs(node.right, s)

            return node.val
        
        dfs(root, 0)
        return total_sum


        
solution = Solution()
answer = solution.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)))
print(answer)