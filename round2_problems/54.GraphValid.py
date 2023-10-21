from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 7:55
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()

        def dfs(node):
            seen.add(node)
            for neighbor in adj[node]:
                if neighbor in seen:
                    continue

                dfs(neighbor)

        dfs(0)
        return len(seen) == n

        
solution = Solution()
answer = solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]])
print(answer)