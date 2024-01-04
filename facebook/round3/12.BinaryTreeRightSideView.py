from typing import List, Optional

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
    # Time: started 1:19
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth, pos):
            if node is None:
                return
            
            if depth == len(result):
                result.append(node.val)
            
            dfs(node.right, depth + 1, pos + 1)
            dfs(node.left, depth + 1, pos - 1)

        dfs(root, 0, 0)
        return result



        
solution = Solution()
answer = solution.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))))
print(answer)