from typing import List
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(h)
    # Space Complexity: O(1)
    # Time: 9:00
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def get_depth(node):
            depth = 0
            while node:
                node = node.parent
                depth += 1
            return depth
        
        p_depth = get_depth(p)
        q_depth = get_depth(q)

        while p_depth > q_depth:
            p = p.parent
            p_depth -= 1
        while q_depth > p_depth:
            q = q.parent
            q_depth -= 1

        queue = deque([(p, q)])

        while queue:
            p_node, q_node = queue.popleft()

            if p_node == q_node:
                return p_node
            
            queue.append((p_node.parent, q_node.parent))



    # Runtime Complexity: O(h)
    # Space Complexity: O(h)
    # Time: 9:00
    def lowestCommonAncestor2(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()

        def dfs(node):
            if node is None:
                return
            
            if node in seen:
                return node
            
            seen.add(node)
            
            return dfs(node.parent)
        
        dfs(p)
        return dfs(q)
        
solution = Solution()
n3 = Node(3)
n5 = Node(5)
n1 = Node(1)
n6 = Node(6)
n2 = Node(2)
n0 = Node(0)
n8 = Node(8)
n7 = Node(7)
n4 = Node(4)

# Setting up left and right children
n3.left, n3.right = n5, n1
n5.left, n5.right, n5.parent = n6, n2, n3
n1.left, n1.right, n1.parent = n0, n8, n3
n6.parent = n5
n2.left, n2.right, n2.parent = n7, n4, n5
n0.parent = n1
n8.parent = n1
n7.parent = n2
n4.parent = n2

# Example nodes to find LCA for
p = n5  # Node with value 5
q = n4  # Node with value 1
answer = solution.lowestCommonAncestor(p, q)
print(answer)