from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 11:00
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        courses_visited = 0

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        queue = deque()
        # find all 0 indegree nodes and add to queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            n = queue.popleft()
            courses_visited += 1

            for neighbor in adj[n]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == courses_visited

        
solution = Solution()
answer = solution.canFinish(4, [[1,0],[3,0],[2,3],[1,2]])
print(answer)