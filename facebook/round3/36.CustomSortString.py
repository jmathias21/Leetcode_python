from typing import List
from collections import Counter

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:39
    def customSortString(self, order: str, s: str) -> str:
        sorted_str = []
        frequencies = Counter(s)

        for char in order:
            if char in frequencies:
                sorted_str.extend([char] * frequencies[char])
                frequencies[char] = 0

        for char, freq in frequencies.items():
            if freq > 0:
                sorted_str.extend([char] * frequencies[char])

        return "".join(sorted_str)
                
        
solution = Solution()
answer = solution.customSortString(order = "cba", s = "abcd")
print(answer)