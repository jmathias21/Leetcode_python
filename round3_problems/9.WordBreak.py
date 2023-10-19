from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:00
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                if i >= len(word) - 1:
                    if dp[i - len(word) + 1] and s[i - len(word) + 1:i + 1] == word:
                        dp[i + 1] = True

        return dp[len(s)]


        
solution = Solution()
answer = solution.wordBreak("leetcode", ["leet","code"])
answer = solution.wordBreak("catsanddog", ["cats","dog","sand","and","cat"])
answer = solution.wordBreak("aaa", ["aa","aaa"])
print(answer)