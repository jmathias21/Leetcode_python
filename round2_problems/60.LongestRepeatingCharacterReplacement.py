from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 3:25
    def characterReplacement(self, s: str, k: int) -> int:
        # track frequency of letters as we go
        # at current index, if the i - frequency < k, then we move left up 1 and update frequency
        frequencies = defaultdict(int)
        max_frequency = 0
        longest = 0
        left = 0

        for i in range(len(s)):
            frequencies[s[i]] += 1
            max_frequency = max(max_frequency, frequencies[s[i]])

            if i - left - max_frequency < k:
                longest = max(longest, (i - left) + 1)
            else:
                frequencies[s[left]] -= 1
                left += 1
            
        return longest


        
solution = Solution()
answer = solution.characterReplacement("BAAAB", 2)
print(answer)