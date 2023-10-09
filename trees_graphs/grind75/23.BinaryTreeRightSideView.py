from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-right-side-view/
# Tags: BFS, Binary Tree, Right Side View
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(h)
    # Time: 25:00
    #
    # Uses DFS to traverse the right-most nodes of the tree first. If we haven't yet added a node
    # for the current level, we add it to our answer
    def rightSideViewUsingDFS(self, root: Optional[TreeNode]) -> List[int]:
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

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 25:00
    #
    # Performs BFS to find the rightmost node at each level. We know a node is
    # the rightmost node at that level if its the last node to be processed at
    # that level
    def rightSideViewUsingBFS(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        rightmost = {}

        while queue:
            node, depth = queue.popleft()

            # set the current rightmost node's value for this depth. The last node
            # to be processed at this level will be the rightmost node
            rightmost[depth] = node.val

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        answer = []
        for _, val in rightmost.items():
            answer.append(val)

        return answer
            
        
solution = Solution()
answer = solution.rightSideViewUsingDFS(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)))
answer = solution.rightSideViewUsingDFS(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, TreeNode(4))))
print(answer)