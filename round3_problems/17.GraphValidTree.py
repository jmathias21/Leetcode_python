from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 22:00
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True

        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)

        dfs(0)
        return len(seen) == n

        
solution = Solution()
#answer = solution.validTree(4, [[0,1],[2,3]])
answer = solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
#answer = solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]])
print(answer)