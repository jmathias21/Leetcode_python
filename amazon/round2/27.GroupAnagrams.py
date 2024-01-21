from collections import Counter, defaultdict
from typing import List

# 
# Tags: 
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            hash = [0] * 26
            for char in s:
                hash[ord(char) - ord('a')] += 1
            d[tuple(hash)].append(s)

        return d.values()

        
solution = Solution()
answer = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
answer = solution.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"])
print(answer)