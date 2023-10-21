from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/path-sum-ii/
# Tags: Recursive DFS, Binary Tree
class Solution:

    # Runtime Complexity: O(N ^ 2)
    # Space Complexity: O(N)
    # Time: 23:00
    #
    # Perform DFS, tracking current sum and the current array of node values. When we find
    # an end leaf node with the target sum, we add the current array to our output
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def dfs(node, arr, s):
            if node is None:
                return
            
            arr.append(node.val)
            
            s += node.val
            if s == targetSum and node.left is None and node.right is None:
                output.append(arr.copy())
            else:
                dfs(node.left, arr, s)
                dfs(node.right, arr, s)

            arr.pop()

        dfs(root, [], 0)
        return output

        
solution = Solution()
answer = solution.pathSum(TreeNode(-2, None, TreeNode(-3)), -5)
answer = solution.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22)
print(answer)