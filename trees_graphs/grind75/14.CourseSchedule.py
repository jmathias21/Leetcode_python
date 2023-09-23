from typing import List
from collections import deque

# https://leetcode.com/problems/course-schedule/
# Resources: https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3886/
# Tags: Kahns algorithm for topological sorting, cyclical graph, DFS, post-order traversal
class Solution:

    # Runtime Complexity: O(m + n) where n is the # of courses and m is the # of edges (pre-reqs)
    # Space Complexity: O(m + n)
    # Time: Not timed
    #
    # This solution uses a simplified version of Kahn's algorithm for topological sorting
    # to determine if there's a cycle. Its simplified because we don't need to sort the entire graph,
    # but rather just determine if its impossible to sort
    def canFinishUsingKahnsAlg(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # keep track of the in-degree value for each course
        indegree = [0] * numCourses

        # keep track of dependents for each course (i.e. courses that depend on it).
        # This means the parent course is the pre-requisite
        adj = [[] for _ in range(numCourses)]

        # build the graph from the pre-requisites
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        # Kahn's Algorithm for Topological Sorting (simplified because we just need to
        # know if it's cyclical, not actually sort it)

        # Find all 0 in-degree nodes and add them to the queue
        queue = deque()
        for i in range(0, numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodesVisited = 0

        # Pop the next node and search for nodes that are children of the popped node.
        # When we find one, subtract 1 from its in-degree and then add it to the queue
        # if the in-degree now equals 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses
    
    # Runtime Complexity: O(m + n) where n is the # of courses and m is the # of edges (pre-reqs)
    # Space Complexity: O(m + n)
    # Time: Not timed
    #
    # This solution demonstrates a DFS post-order traversal of a directed graph using
    # recursion in order to find out if it has a cycle. We build up an array of which
    # nodes have been seen in the current stack, and we pass that along in each recursive call.
    # If we see the node twice in the same stack, then we know there's a cycle
    def canFinishUsingDFSRecursive(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        inStack = [False] * numCourses

        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        # loop through every single course (node) to make sure that we've visited
        # every node in our DFS
        for course in range(numCourses):
            if self.isCycleRec(course, adj, visited, inStack):
                return False
            
        return True
    
    def isCycleRec(self, node, adj, visited, inStack):
        # if we've seen this node before inside of the current stack,
        # then there's a cycle. This must be checked before we've checked
        # whether w've visted this node before
        if inStack[node]:
            return True

        if visited[node]:
            return False
        
        visited[node] = True
        inStack[node] = True
        
        for neighbor in adj[node]:
            if self.isCycleRec(neighbor, adj, visited, inStack):
                return True

        # after we handle all of the node's neighbors, we remove it from the stack
        inStack[node] = False

        return False
    
    # Runtime Complexity: O(m + n) where n is the # of courses and m is the # of edges (pre-reqs)
    # Space Complexity: O(m + n)
    # Time: Not timed
    #
    # This solution demonstrates a DFS post-order traversal of a directed graph using an
    # iterative approach rather than a recursive approach. We build up an array of which
    # nodes have been seen in the current stack, and we use that to see if we trip over
    # the same node twice in that stack. If we do, we know there's a cycle
    def canFinishUsingDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        inStack = [False] * numCourses

        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        # loop through every single course (node) to make sure that we've visited
        # every node in our DFS
        for course in range(numCourses):
            if visited[course]:
                continue
            
            stack = [course]
            while stack:
                # peek the top of the stack. We don't pop it yet because we want to
                # use our stack to perform a post-order traversal. This means we don't
                # actually process the node until all of it's neighbors have been processed
                node = stack[-1]
                
                # if we visit a node that we've seen before, we can pop it off the stack
                # so it never gets processed again
                if visited[node]:
                    inStack[node] = False
                    stack.pop()
                    continue

                visited[node] = True
                inStack[node] = True

                hasUnvisitedNeighbor = False

                for neighbor in adj[node]:
                    if inStack[neighbor]:  # Found a cycle
                        return False
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        hasUnvisitedNeighbor = True

                if not hasUnvisitedNeighbor:
                    # if all neighbors have been visited, we can process the current node since
                    # this is a post-order traversal. For this node, we want to indicate that
                    # its no longer in the stack
                    inStack[node] = False
                    stack.pop()

        return True

        
solution = Solution()
#answer = solution.canFinishUsingDFS(2, [[1,0]])
answer = solution.canFinishUsingDFSRecursive(5, [[1,4],[2,4],[3,1],[3,2]])
#answer = solution.canFinish(5, [[4, 5], [5, 0], [4, 1], [7, 9]])
print(answer)


# Example for canFinishUsingKahnsAlg: prerequisites = [[1,4],[2,4],[3,1],[3,2]], numCourses = 5

#  1 <- 4
#  v    v
#  3 <- 2
# This diagram shows pre-requisite courses pointing at courses that depend on them

# adj = [[], [3], [3], [], [1, 2]] <-- The values are the courses that depend on that pre-requisite
#        0    1    2   3   4  <-- The array indexes are the pre-requisite courses
# e.g. Course 4 is the pre-requisite for courses 1 and 2

# indegree = [0, 1, 1, 2, 0]
#             0, 1, 2, 3, 4 <-- The array indexes are the course numbers
# e.g. Course 3 has an in-degree of 2, meaning two courses are pointing at it. So course 3
# has two pre-requisites: courses 1 and 2

# Now we find all 0 in-degree nodes and add them to queue: [0, 4]

# Pop 0 off queue. No neighbors
# Pop 4 off queue. It has neighbors 1 and 2. Subtract 1 from in-degree for both.
    # Neighbor 1 now has an in-degree of 0. Add to queue.
    # Neighbor 2 now has an in-degree of 1. Add to queue.
# Pop 1 off queue. It has neighbor 3. Subtract 1 from in-degree.
    # Neighbor 3 now has an in-degree of 1. Do nothing
# Pop 2 off queue. It has neighbor 3. Subtract 1 from in-degree.
    # Neighbor 3 now has an in-degree of 0. Add to queue
# Pop 3 off queue. It has no neighbors

# Return the total nodes visited (total nodes popped off queue) = 5
# total nodes visited (5) == numCourses (5) = True