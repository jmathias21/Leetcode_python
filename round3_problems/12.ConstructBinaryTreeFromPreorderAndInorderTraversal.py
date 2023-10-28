from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:30
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map = {}

        for i in range(len(preorder)):
            map[inorder[i]] = i

        def dfs(i, left, right):
            if left > right: return None, i

            node_val = preorder[i]
            node = TreeNode(preorder[i])
            i += 1

            node.left, i = dfs(i, left, map[node_val] - 1)
            node.right, i = dfs(i, map[node_val] + 1, right)
            return node, i

        return dfs(0, 0, len(inorder) - 1)[0]

        
solution = Solution()
answer = solution.buildTree([3,1,2,4], [1,2,3,4])
answer = solution.buildTree([1,2], [1,2])
answer = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(answer)