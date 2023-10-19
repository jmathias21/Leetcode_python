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
    # Time: started 3:21
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_map = {}
        preorder_index = 0

        for i in range(len(preorder)):
            root_map[inorder[i]] = i

        def dfs(left, right):
            nonlocal preorder_index

            if left > right:
                return None
            
            new_node = TreeNode(preorder[preorder_index])

            preorder_index += 1

            new_node.left = dfs(left, root_map[new_node.val] - 1)
            new_node.right = dfs(root_map[new_node.val] + 1, right)
            return new_node

        return dfs(0, len(inorder) - 1)


        
solution = Solution()
answer = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(answer)

# root = 3
# 