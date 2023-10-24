from typing import List

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Tags: Union Find, Disjoint Set Union (DSU)
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 20:00
    #
    # Union all edges together and then count the roots
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = set()
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x < root_y:
                parent[root_y] = root_x
            elif root_x > root_y:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x

        for edge in edges:
            union(edge[0], edge[1])

        # find unique roots
        for i in range(n):
            roots.add(find(i))

        return len(roots)

        
solution = Solution()
answer = solution.countComponents(5, [[0,1],[1,2],[3,4]])
print(answer)