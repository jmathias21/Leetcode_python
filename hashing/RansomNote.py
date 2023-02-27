
from typing import List
from collections import defaultdict

# https://leetcode.com/problems/ransom-note/editorial/
# Tags: Hash Map
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(int)

        for c in magazine:
            d[c] += 1

        for c in ransomNote:
            if d[c] < 0:
                return False

        if sum(d.values()) <= 0:
            return True
        else:
            return False

            
solution = Solution()
answer = solution.canConstruct("aab", "baba")
print(answer)

# Input: ransomNote = "aa", magazine = "aab"
# Output: true