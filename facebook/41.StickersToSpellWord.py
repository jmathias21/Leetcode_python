from typing import List
from collections import Counter

# https://leetcode.com/problems/stickers-to-spell-word/
# Tags: DFS, Top-down dynamic programming
class Solution:

    # Runtime Complexity: O(n^2 * n)
    # Space Complexity: O(n)
    # Time: Not timed
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counters = []
        for sticker in stickers:
            sticker_counters.append(Counter(sticker))

        dp = {}

        def dfs(t, sticker):
            if t in dp:
                return dp[t]

            result = 1 if sticker else 0
            remaining = ""
            for char in t:
                if char in sticker and sticker[char] > 0:
                    sticker[char] -= 1
                else:
                    remaining += char

            if remaining:
                stickers_used = float('inf')
                for s in sticker_counters:
                    if remaining[0] in s:
                        stickers_used = min(stickers_used, dfs(remaining, s.copy()))
                result += stickers_used
                dp[remaining] = stickers_used
            return result

        result = dfs(target, {})
        return result if result != float('inf') else -1

        
solution = Solution()
answer = solution.minStickers(["with","example","science"], "thehat")
print(answer)