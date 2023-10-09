from typing import List
from collections import deque

# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:03
    def canFinishUsingKahns(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        # check for 0 indegree nodes and add to queue
        # pop top, find all prereqs, and subtract indegree by 1
        # repeat

        queue = deque()
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        zero_course_count = 0

        while queue:
            zero_course = queue.popleft()
            zero_course_count += 1

            for course in adj[zero_course]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return zero_course_count == numCourses

    
    # Runtime Complexity: O(m + n)
    # Space Complexity: O(m + n)
    # Time: started 2:03
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        visited = set()

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course, course_stack):
            if course_stack[course]:
                return True
            
            if course in visited:
                return False

            visited.add(course)

            for prereq in adj[course]:
                course_stack[course] = True
                if dfs(prereq, course_stack):
                    return True
                course_stack[course] = False

            return False

        is_cycle = False
        for course in range(numCourses):
            is_cycle = is_cycle or dfs(course, [False] * numCourses)

        return not is_cycle
            
        
solution = Solution()
answer = solution.canFinish(2, [[1, 0]])
answer = solution.canFinish(3, [[0, 1], [1, 2], [2, 0]])
answer = solution.canFinishUsingKahns(5, [[1,4],[2,4],[3,1],[3,2]])
print(answer)