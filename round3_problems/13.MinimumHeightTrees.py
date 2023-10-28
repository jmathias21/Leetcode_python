from collections import defaultdict, deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 18:00
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(set)
        remaining_nodes = n

        # O(e)
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])

        queue = deque()
         # O(e)
        for i in range(len(adj)):
            if len(adj[i]) == 1:
                queue.append(i)

        while remaining_nodes > 2:
            new_queue = deque()
            # O(e)
            while queue:
                node = queue.popleft()

                child = adj[node].pop()
                del adj[node]
                # O(e)
                adj[child].remove(node)
                remaining_nodes -= 1

                if len(adj[child]) == 1:
                    new_queue.append(child)
            queue = new_queue

        return [k for k in adj.keys()]

        
solution = Solution()
answer = solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
print(answer)