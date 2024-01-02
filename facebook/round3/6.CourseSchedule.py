from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/course-schedule/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:42
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegrees = [0] * numCourses
        nodes_visited = 0

        # build adj list
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegrees[prereq[0]] += 1

        # find 0 in-degree nodes, remove them, and update in-degree
        queue = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            nodes_visited += 1

            for neighbor in adj[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return nodes_visited == numCourses


            


        
solution = Solution()
answer = solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])
print(answer)