from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:10
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        seen = set()
        in_stack = set()

        def dfs(node):
            if node in in_stack:
                return True

            if node in seen:
                return False
            
            seen.add(node)
            in_stack.add(node)
            
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True
                
            in_stack.remove(node)

            return False

        for i in range(numCourses):
            if dfs(i):
                return False
            
        return True

        
solution = Solution()
#answer = solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])
#answer = solution.canFinish(2, [[1,0],[0,1]])
answer = solution.canFinish(2, [[1,1]])
print(answer)