from collections import defaultdict

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 7:17
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        max_frequency = 0
        answer = 0
        left = 0

        for i in range(len(s)):
            char = s[i]
            frequencies[char] += 1
            max_frequency = max(max_frequency, frequencies[char])

            window_size = i - left
            if window_size - max_frequency < k:
                answer = (i - left) + 1
            else:
                frequencies[s[left]] -= 1
                left += 1

        return answer


        
solution = Solution()
answer = solution.characterReplacement("ABAA", 0)
#answer = solution.characterReplacement("ABAB", 2)
answer = solution.characterReplacement("AABABBA", 1)
print(answer)