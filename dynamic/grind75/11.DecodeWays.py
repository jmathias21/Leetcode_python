from functools import lru_cache
from typing import List

# https://leetcode.com/problems/decode-ways/editorial/
# Tags: Backtracking, Recursion, Dynamic Programming
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def numDecodings(self, s: str) -> int:
        memo = [-1] * (len(s) + 2)

        def backtrack(i):  
            if memo[i] != -1:
                return memo[i]
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            answer = backtrack(i + 1)
            if int(s[i:i + 2]) <= 26:
                answer += backtrack(i + 2)

            memo[i] = answer

            return answer

        answer = backtrack(0)
        return answer
        
solution = Solution()
answer = solution.numDecodings("226")
print(answer)