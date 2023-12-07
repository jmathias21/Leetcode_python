from typing import List
from collections import defaultdict

# https://leetcode.com/problems/group-shifted-strings/
# Tags: Hash Map
class Solution:

    # Runtime Complexity: O(n * max(k))
    # Space Complexity: O(n * max(k))
    # Time: Not timed
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for string in strings:
            # get the diff between first character in string and 'a' so that we can adjust
            # the current string to start with 'a'
            diff = ord('a') - ord(string[0])
            hash_arr = []

            # apply the diff so that the string gets adjusted to start with 'a'. We mod the ordinal
            # so that if a shift loops (i.e. "az", "ba"), they will equal the same hash
            for i in range(len(string)):
                char_hash = chr((diff + ord(string[i])) % 26)
                hash_arr.append(char_hash)

            hash = "".join(hash_arr)
            groups[hash].append(string)

        return [group for group in groups.values()]

        
solution = Solution()
answer = solution.groupStrings(["az","ba"])
answer = solution.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])
print(answer)