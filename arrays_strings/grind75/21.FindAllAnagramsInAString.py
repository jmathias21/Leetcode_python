from collections import defaultdict
from typing import List

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Tags: Sliding window
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1) at most 26 characters
    # Time: Not timed
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)

        # if p is longer than s, it's impossible to find an anagram within s
        if p_len > s_len:
            return []

        s_map = defaultdict(int)
        p_map = defaultdict(int)
        output = []

        # set the char counts within our initial sliding window for each set
        for i in range(p_len):
            s_map[s[i]] += 1
            p_map[p[i]] += 1

        # move sliding window to the right, maintaining a dictionary of the counts of
        # each character in the sliding window. If the s and p dictionaries match,
        # we add the left index of the sliding window to our output
        for i in range(p_len - 1, s_len):
            left = (i - p_len) + 1

            if i >= p_len:
                s_map[s[i]] += 1
                s_map[s[left - 1]] -= 1
                if s_map[s[left - 1]] == 0:
                    del s_map[s[left - 1]]

            if s_map == p_map:
                output.append(left)

        return output

        
solution = Solution()
answer = solution.findAnagrams("abab", "ab")
answer = solution.findAnagrams("cbaebabacd", "abc")
print(answer)