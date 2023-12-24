from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []

# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        start_node = None

        def build_graph(node, parent):
            if node is None:
                return
            
            new_node = Node(node.val)
            if parent:
                new_node.neighbors.append(parent)

            if node.val == start:
                nonlocal start_node
                start_node = new_node
            
            left = build_graph(node.left, new_node)
            right = build_graph(node.right, new_node)
            if left: new_node.neighbors.append(left)
            if right: new_node.neighbors.append(right)

            return new_node

        build_graph(root, None)

        visited = set()
        queue = deque([(start_node, 0)])
        max_depth = 0
        while queue:
            node, depth = queue.popleft()

            if node in visited:
                continue

            max_depth = max(max_depth, depth)

            visited.add(node)
            for neighbor in node.neighbors:
                queue.append((neighbor, depth + 1))

        return max_depth


        
solution = Solution()
answer = solution.amountOfTime(TreeNode(1, TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10), TreeNode(6))), 3)
print(answer)