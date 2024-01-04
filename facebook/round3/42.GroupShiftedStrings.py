from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n * max(k))
    # Space Complexity: O(n * max(k))
    # Time: 
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strings:
            hash = []
            for char in s:
                hash.append(str((ord(char) - ord(s[0])) % 26))
            d[",".join(hash)].append(s)

        return [x for x in d.values()]

        
solution = Solution()
answer = solution.groupStrings(["az","ba"])
answer = solution.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])
print(answer)