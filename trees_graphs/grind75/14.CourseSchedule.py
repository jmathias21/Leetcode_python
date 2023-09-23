from typing import List
from collections import deque

# https://leetcode.com/problems/course-schedule/
# Tags: Kahns algorithm for topological sorting, cyclical graph, DFS, post-order traversal
class Solution:

    # Runtime Complexity: O(m + n) where n is the # of courses and m is the # of edges (pre-reqs)
    # Space Complexity: O(m + n)
    # Time: Not timed
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
    # This solution demonstrates a DFS post-order traversal of a directed graph using an
    # iterative approach rather than a recursive approach. We build up an array of which
    # needs have been seen in the current stack, and we use that to see if we trip over
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

                # if the current node has already been seen in the current stack, we
                # know this graph has a cycle
                if inStack[node]:
                    return False
                
                # if we visit a node that we've seen before, we can pop it off the stack
                # so it never gets processed again
                if visited[node]:
                    stack.pop()
                    continue

                visited[node] = True
                inStack[node] = True

                hasUnvisitedNeighbor = False

                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

                        # these two lines make sure we process this neighbor before we process
                        # the next neighbors. It helps turn this from a BFS into a DFS
                        hasUnvisitedNeighbor = True
                        break

                if not hasUnvisitedNeighbor:
                    # if all neighbors have been visited, we can process the current node since
                    # this is a post-order traversal. For this node, we want to indicate that
                    # its no longer in the stack
                    inStack[node] = False
                    stack.pop()

        return True


        
solution = Solution()
answer = solution.canFinishUsingDFS(5, [[1,4],[2,4],[3,1],[3,2]])
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

#-----------------------------------------------------------------------------------------

# Example for canFinishUsingDFS: prerequisites = [[1,4],[2,4],[3,1],[3,2]], numCourses = 5

#  1 <- 4
#  v    v
#  3 <- 2
# This diagram shows pre-requisite courses pointing at courses that depend on them

#