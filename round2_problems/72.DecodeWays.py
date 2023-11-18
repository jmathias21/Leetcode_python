from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 16:00
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return 1

            res = 0
            if int(s[i]) > 0:
                res += dfs(i + 1)

                if i + 1 < len(s) and int(s[i] + s[i + 1]) <= 26:
                    res += dfs(i + 2)

            memo[i] = res
            return memo[i]

        return dfs(0)
        
solution = Solution()
answer = solution.numDecodings("06")
answer = solution.numDecodings("226")
print(answer)