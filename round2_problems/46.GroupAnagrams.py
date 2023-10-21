from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:28
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for str in strs:
            d[''.join(sorted(str))].append(str)

        return list(d.values())
        
solution = Solution()
answer = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(answer)

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]