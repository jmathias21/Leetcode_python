from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# https://leetcode.com/problems/clone-graph/
# Tags: BFS, connected graph, undirected graph
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Perform a BFS across all nodes, using a hash map to build out
    # the cloned nodes as we traverse the nodes
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # use a dictionary to keep track of cloned nodes for a specific node
        # value (i.e. the key)
        clone_map = {node.val: Node(node.val)}

        # use a queue so we can perform a BFS to traverse all of the # nodes
        queue = deque([node])

        while queue:
            n = queue.popleft()

            for neighbor in n.neighbors:
                # for each neighbor, create a clone of the neighbor if one doesn't
                # already exist and append it to the queue
                if neighbor.val not in clone_map:
                    clone_map[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add the cloned neighbor to the neighbors list of the cloned
                # current node. We can guarantee that we won't append the same
                # neighbor more than once because every node will only be visted
                # once
                clone_map[n.val].neighbors.append(clone_map[neighbor.val])

        return clone_map[node.val]
        
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

# Example:

# [Original Graph]          [Cloned Graph (Evolving)]
# 1 -- 2                    
# |    |     ====>          1  
# 4 -- 3                   

# 1. The clone of node1 is created, resulting in cloned_node1 with value 1.

# [Original Graph]          [Cloned Graph (Evolving)]
# 1 -- 2                    1  
# |    |     ====>          |
# 4 -- 3                    4  

# 2. Node1's first neighbor, node4, is checked. A clone for it, cloned_node4, 
# is created and connected to cloned_node1.

# [Original Graph]          [Cloned Graph (Evolving)]
# 1 -- 2                    1  -- 2
# |    |     ====>          |
# 4 -- 3                    4

# 3. Node1's next neighbor, node2, is checked. A clone for it, cloned_node2,
# is created and connected to cloned_node1.

# [Original Graph]          [Cloned Graph (Evolving)]
# 1 -- 2                    1  -- 2
# |    |     ====>          |    |
# 4 -- 3                    4    3

# 4. Node2's next neighbor, node3, is checked (since node1 already has a clone).
# A clone for node3, cloned_node3, is created and connected to cloned_node2.

# [Original Graph]          [Cloned Graph (Evolving)]
# 1 -- 2                    1  -- 2
# |    |     ====>          |    |
# 4 -- 3                    4 -- 3

# 5. Node4 is dequeued and its neighbors (nodes 1 and 3) are checked. Both already
# have clones, so it gets connected to both cloned_node1 and cloned_node3.

# By the end of this process, we have a cloned graph that mirrors the structure of
# the original graph but consists of new Node instances.