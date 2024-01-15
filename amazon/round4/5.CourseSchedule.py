from collections import defaultdict, deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(m + n)
    # Space Complexity: O()
    # Time: started 11:01
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degrees = [0] * numCourses
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            in_degrees[prereq[0]] += 1

        queue = deque()
        for course, indegree in enumerate(in_degrees):
            if indegree == 0:
                queue.append(course)

        nodes_visited = 0
        while queue:
            course = queue.popleft()
            nodes_visited += 1
            
            if in_degrees[course] == 0:
                for neighbor in adj[course]:
                    in_degrees[neighbor] -= 1
                    if in_degrees[neighbor] == 0:
                        queue.append(neighbor)

        return nodes_visited == numCourses


        
solution = Solution()
answer = solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])
print(answer)