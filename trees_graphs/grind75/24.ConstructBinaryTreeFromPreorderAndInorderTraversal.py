from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Tags: DFS, Binary Tree, Pre-order traversal, In-order traversal
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # You are to rebuild a binary tree using two given lists of numbers (preorder and inorder), which represent
    # two different ways the tree's nodes are sequenced. Start with the first number in the preorder list as the
    # root, then recursively organize the remaining numbers into left and right subtrees based on their positions
    # in the inorder list, until the tree is reconstructed.
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
answer = solution.buildTree([1,2], [1,2])
answer = solution.buildTree([1,2], [2,1])
answer = solution.buildTree([3,9,1,2,20,15,7], [1,9,2,3,15,20,7])
print(answer)