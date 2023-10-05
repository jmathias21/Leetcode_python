from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    # Runtime Complexity: O(n + m)
    # Space Complexity: O(n)
    # Time: 18:00
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
             return None

        visited = {}

        def dfs(node, clone):
            if node.val in visited:
                return visited[node.val]

            clone = Node(node.val)

            visited[node.val] = clone

            for neighbor in node.neighbors:
                    clone.neighbors.append(dfs(neighbor, clone))

            return clone
        
        clone = dfs(node, [])
        return clone
        

solution = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.append(n2)
n1.neighbors.append(n4)

n2.neighbors.append(n1)
n2.neighbors.append(n3)

n3.neighbors.append(n2)
n3.neighbors.append(n4)

n4.neighbors.append(n1)
n4.neighbors.append(n3)

answer = solution.cloneGraph(n1)
print(answer)