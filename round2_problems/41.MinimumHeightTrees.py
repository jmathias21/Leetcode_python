from collections import defaultdict, deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:50
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # find all nodes with one connection
        # Remove them until two or less (remove in batches)

        if n == 1:
            return [0]

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        leaves = deque()

        for i in range(len(adj)):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = deque()
            while leaves:
                leaf = leaves.popleft()

                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)

                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
                        
        
solution = Solution()
answer = solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
print(answer)