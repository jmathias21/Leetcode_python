# https://leetcode.com/problems/substring-with-largest-variance/
# Tags: Kadane's Algorithm
class Solution:

    # Runtime Complexity: O(k^2 * n) where k is unique characters
    # Space Complexity: O(k)
    # Time: Not timed
    def largestVariance(self, s: str) -> int:
        unique_chars = list(set(s))
        pairs = []
        for i in range(len(unique_chars)):
            for j in range(len(unique_chars)):
                if i != j:
                    pairs.append((unique_chars[i], unique_chars[j]))

        max_variation = 0
        def solve_pair(a, b, str):
            nonlocal max_variation
            f1 = None
            f2 = None

            for _ in range(2):
                f1, f2 = 0, 0
                for char in str:
                    if char != a and char != b:
                        continue

                    if f1 - f2 < 0:
                        f1 = f2 = 0

                    if char == a:
                        f1 += 1
                    elif char == b:
                        f2 += 1

                    if f2 != 0:
                        max_variation = max(max_variation, f1 - f2)
                str = str[::-1]

        for a, b in pairs:
            solve_pair(a, b, s)

        return max_variation

        
solution = Solution()
answer = solution.largestVariance("lripaa")
answer = solution.largestVariance("aababbb")
print(answer)