from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 12:04
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        path = []
        
        for dir in dirs:
            if dir == "":
                continue

            if dir == "..":
                if path:
                    path.pop()
            elif dir != ".":
                path.append(dir)

        return "/" + "/".join(path)
    
        
solution = Solution()
# answer = solution.simplifyPath("/home/")
# answer = solution.simplifyPath("/home//foo/../")
answer = solution.simplifyPath("/../")
print(answer)