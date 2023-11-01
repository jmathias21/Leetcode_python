from collections import defaultdict
from typing import List

# https://leetcode.com/problems/group-anagrams/
# Tags: Tuples, Anagrams
class Solution:

    # Runtime Complexity: O(n * k * logk)
    # Space Complexity: O(n * k)
    # Time: Not timed
    #
    # For each string, sort the chars and append the string to the sorted key. e.g.
    # "eat" and "ate" both have a key of "aet", and that key would store and array
    # of ["eat", "ate"]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            groups[tuple(sorted(str))].append(str)

        return groups.values()

        
solution = Solution()
answer = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(answer)