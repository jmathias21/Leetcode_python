from collections import deque
from typing import List

# https://leetcode.com/problems/course-schedule-ii/
# Tags: Kahns algorithm for topological sorting, cyclical graph, BFS, post-order traversal
class Solution:

    # Runtime Complexity: O(V + E)
    # Space Complexity: O(V + E)
    # Time: 25:00
    #
    # Build adjacency list and in-degree array and find zero in-degree nodes. Then perform BFS on
    # zero-indegree nodes and remove them from array, while identifying more zero-indegree nodes that arose
    # from the previous ones we removed. The order of in-degree nodes that we identify is the order with which
    # should take our class. If the total amount of zero in-degree nodes we find is not equal to the number
    # of courses, then there's a cycle in the graph and we return empty
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        output = []

        while queue:
            n = queue.popleft()
            output.append(n)

            neighbors = adj[n]

            for neighbor in neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return output if len(output) == numCourses else []


        
solution = Solution()
answer = solution.findOrder(2, [[1,0]])
answer = solution.findOrder(3, [[1,0],[1,2],[0,1]])
answer = solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(answer)