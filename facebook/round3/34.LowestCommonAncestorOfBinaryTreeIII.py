from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:06
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()

        def rec(node):
            if node is None:
                return None
        
            if node in visited:
                return node
            
            visited.add(node)
            return rec(node.parent)

        rec(p)
        return rec(q)

        
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