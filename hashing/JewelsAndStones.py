
from typing import List

# https://leetcode.com/problems/jewels-and-stones/editorial/
# Tags: Hash Set
class Solution:
    
    # Runtime Complexity: O(n + m)
    # Space Complexity: O(1)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0

        d = set(jewels)

        for c in stones:
            if c in d:
                total += 1

        return total


            
solution = Solution()
answer = solution.numJewelsInStones("aA", "aAAbbbb")
print(answer)

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3