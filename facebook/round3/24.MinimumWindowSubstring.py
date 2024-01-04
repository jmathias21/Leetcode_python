from typing import List
from collections import Counter, defaultdict

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 6:03
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        window_frequencies = defaultdict(int)
        t_frequencies = Counter(t)
        needed = sum(t_frequencies.values())
        haves = 0
        result = (-1, -1, float('inf'))

        for i, char in enumerate(s):

            if char in t_frequencies:
                window_frequencies[char] += 1
                if window_frequencies[char] == t_frequencies[char]:
                    haves += t_frequencies[char]

            while haves == needed:
                if i - left < result[2]:
                    result = (left, i, i - left)

                if s[left] in t_frequencies:
                    window_frequencies[s[left]] -= 1
                    if window_frequencies[s[left]] < t_frequencies[s[left]]:
                        haves -= t_frequencies[s[left]]
                left += 1

        return s[result[0]:result[1] + 1] if result[0] != -1 else ""

        
solution = Solution()
answer = solution.minWindow("aa", "aa")
answer = solution.minWindow("ADOBECODEBANC", "ABC")
print(answer)