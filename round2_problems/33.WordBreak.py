from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 8:44
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s) + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break

        return dp[n]

        
solution = Solution()
answer = solution.wordBreak("leetcodeleet", ["leet","code"])
#answer = solution.wordBreak("aaaaaaa", ["aaaa","aaa"])
print(answer)