from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# 
# Tags: 
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:        
        visited = {}
        def dfs(node):
            if node is None:
                return
            
            if node in visited:
                return visited[node]
            
            new_node = Node(node.val)
            
            visited[node] = new_node
            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor)
                if new_neighbor:
                    new_node.neighbors.append(new_neighbor)

            return new_node

        return dfs(node)

solution = Solution()

node1 = Node(val=1)
node2 = Node(val=2)
node3 = Node(val=3)
node4 = Node(val=4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

answer = solution.cloneGraph(node1)
print(answer)