from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:18
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def rec(start):
            nonlocal memo
            if start in memo:
                return memo[start]

            if start == len(s):
                return True
            
            for word in wordDict:
                end = start + len(word)
                if end <= len(s) and s[start:end] == word and rec(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False
        
        return rec(0)

        
solution = Solution()
answer = solution.wordBreak("applepenapple", ["apple", "pen"])
print(answer)