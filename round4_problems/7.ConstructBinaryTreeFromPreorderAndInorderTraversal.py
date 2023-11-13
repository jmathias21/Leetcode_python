from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Time: started 1:00
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        root_map = {}
        for i in range(len(inorder)):
            root_map[inorder[i]] = i

        def dfs(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            
            node = TreeNode(preorder[preorder_index])
            preorder_index += 1

            node.left = dfs(left, root_map[node.val] - 1)
            node.right = dfs(root_map[node.val] + 1, right)

            return node
        
        return dfs(0, len(preorder) - 1)


        
solution = Solution()
answer = solution.buildTree([1,3,7,6,12,8,9], [7,3,12,6,1,8,9])
print(answer)