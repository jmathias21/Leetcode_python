from collections import Counter

# https://leetcode.com/problems/custom-sort-string/
# Tags: Frequencies
class Solution:

    # Runtime Complexity: O(n + m)
    # Space Complexity: O(n)
    # Time: 26:00
    def customSortString(self, order: str, s: str) -> str:
        frequencies = Counter(s)

        output = []
        for char in order:
            if char in frequencies:
                output.extend([char] * frequencies[char])
                del frequencies[char]

        for char, freq in frequencies.items():
            output.extend([char] * freq)

        return "".join(output)
        
solution = Solution()
answer = solution.customSortString("cba", "abcd")
print(answer)