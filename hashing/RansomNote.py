
from typing import List
from collections import defaultdict

# https://leetcode.com/problems/ransom-note/editorial/
# Tags: Hash Map
class Solution:
    
    # Runtime Complexity: O(m)
    # Space Complexity: O(1) - Never more than 26 characters
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if meagazing is smaller than the ransom note, it's not possible to construct
        # the ransom note from the magazine
        if (len(magazine) < len(ransomNote)):
            return False

        d = defaultdict(int)

        for c in magazine:
            d[c] += 1

        for c in ransomNote:
            d[c] -= 1

            if d[c] < 0:
                return False

        return True

            
solution = Solution()
answer = solution.canConstruct("aab", "baba")
print(answer)

# Input: ransomNote = "aa", magazine = "aab"
# Output: true