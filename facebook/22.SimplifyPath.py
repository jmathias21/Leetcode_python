from typing import List
from collections import deque

# https://leetcode.com/problems/simplify-path/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 35:00
    def simplifyPath(self, path: str) -> str:
        stack = []
        for dir in path.split('/'):
            if dir == "" or dir == ".":
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
        
solution = Solution()
answer = solution.simplifyPath("/../")
answer = solution.simplifyPath("/a/./b/../../c/")
print(answer)