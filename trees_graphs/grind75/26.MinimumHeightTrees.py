from typing import List
from collections import defaultdict, deque

# https://leetcode.com/problems/minimum-height-trees/
# Tags: topological sorting, adjacency list, undirected graph, tree
class Solution:

    # Runtime Complexity: O(n) where n is the number of nodes in the graph
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Find the centroids of the tree by incrementally removing leaf nodes, which are nodes with
    # only one connection. There can only be 1 or 2 centroids in a tree.
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        # find our leaves (nodes with only one connection)
        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        # while we have more than two nodes left, incrementally remove the leaf nodes. If a new
        # leaf node is created by the removing of a leaf node, add it back to our leaves queue
        # for processing
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = deque()

            while leaves:
                leaf = leaves.popleft()

                # leaf only has one neighbor. Pop it off
                neighbor = adj[leaf].pop()

                # Remove the leaf from the neighbor as well
                adj[neighbor].remove(leaf)

                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

        
solution = Solution()
answer = solution.findMinHeightTrees(7, [[3,0],[3,1],[3,2],[3,4],[5,4],[5,6]])
answer = solution.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
print(answer)