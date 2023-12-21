from typing import List

# https://leetcode.com/problems/length-of-the-longest-valid-substring/
# Tags: Hash Set
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(k)
    # Time: Not timed 
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        res = left = 0

        for i in range(len(word)):
            for j in range(max(left, i - 10), i + 1):
                if word[j:i + 1] in forbidden_set:
                    left = j + 1
            res = max(res, i - left + 1)
        return res

        
solution = Solution()
answer = solution.longestValidSubstring("cbaaaabc", ["cb", "aaa"])
print(answer)