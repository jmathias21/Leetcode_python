from typing import List

# https://leetcode.com/problems/graph-valid-tree/
# Tags: Union Find, DFS, adjacency list
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Create adjacency list from edges then perform DFS using "seen" set. The amount of nodes
    # seen must match n, otherwise its either disconnected or cyclic and therefore not a tree
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # graph is not connected or graph might be cyclic
        if len(edges) != n - 1: return False

        # create adjacency list
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        seen = set()

        def dfs(node, parent):
            if node in seen: return True

            seen.add(node)

            for neighbor in adj[node]:
                if neighbor != parent and dfs(neighbor, node):
                    return True
                
            return False
        
        if dfs(0, None):
            return False
        return len(seen) == n

    # Runtime Complexity: O(n * a(n))
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # A valid tree is a connected acyclic graph. We can use Union Find to check both that the graph is 
    # connected with no disjoint subsets, and to ensure there are no cycles. As we union all of the edges 
    # together, if the roots of the two nodes being unioned are the same, it means these nodes are already 
    # connected in the same set, implying a cycle. Thus, the graph is not a tree. 
    # Additionally, for a graph to be a tree with 'n' nodes, it must have exactly 'n - 1' edges. 
    # After processing all edges, if our Union Find structure indicates more than one subset, 
    # the graph isn't fully connected and hence, isn't a tree.
    def validTreeUsingUnionFind(self, n: int, edges: List[List[int]]) -> bool:
        parent = {}
        rank = [0] * n
        num_subsets = n

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal num_subsets
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                num_subsets -= 1
                return True
            else:
                return False

        for edge in edges:
            if not union(edge[0], edge[1]):
                return False

        return num_subsets == 1

        
solution = Solution()
answer = solution.validTree(4, [[0,1],[1,2],[2,0]])
answer = solution.validTree(4, [[0,1],[2,3]])
answer = solution.validTree(5, [[0,1],[2,1],[2,0],[3,4],[4,0]])
answer = solution.validTree(4, [[0,1],[2,3]])
answer = solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]])
answer = solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
print(answer)