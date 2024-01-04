from collections import deque
from typing import List

class Node:
    def __init__(self, x):
        self.val = x
        self.neighbors = []

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 4:22
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        target_node = None

        # turn tree into graph
        def convert_to_graph(node, parent):
            if node is None:
                return
            
            new_node = Node(node.val)
            nonlocal target_node
            if node.val == target.val:
                target_node = new_node

            if parent:
                new_node.neighbors.append(parent)
            
            left = convert_to_graph(node.left, new_node)
            if left:
                new_node.neighbors.append(left)
            right = convert_to_graph(node.right, new_node)
            if right:
                new_node.neighbors.append(right)

            return new_node

        # treverse graph and return all nodes at depth k
        convert_to_graph(root, None)
        queue = deque([(target_node, 0)])
        result = []

        visited = set()
        while queue:
            node, depth = queue.popleft()

            if node in visited:
                continue

            if depth == k:
                result.append(node.val)
                continue

            visited.add(node)
            for neighbor in node.neighbors:
                queue.append((neighbor, depth + 1))

        return result


        
solution = Solution()
answer = solution.distanceK(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                                     TreeNode(1, TreeNode(0), TreeNode(8))), TreeNode(5), 2)
print(answer)