from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n * m * k)
    # Space Complexity: O()
    # Time: 22:00
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                if i >= len(word) - 1 and dp[i - len(word) + 1] and s[i - len(word) + 1:i + 1] == word:
                    dp[i + 1] = True
                    break

        return dp[len(s)]


        
solution = Solution()
answer = solution.wordBreak("a", ["aa","aaa","aaaa","aaaaa","aaaaaa"])
answer = solution.wordBreak("leetcodeleet", ["leet","code"])
print(answer)