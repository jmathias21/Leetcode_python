from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-right-side-view/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(H)
    # Time: started 3:57
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def dfs(node, depth):
            if node is None:
                return
            
            if len(answer) == depth:
                answer.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return answer

        
solution = Solution()
answer = solution.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, TreeNode(4))))
print(answer)