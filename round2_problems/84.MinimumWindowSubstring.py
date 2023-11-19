from collections import defaultdict

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(t + s)
    # Space Complexity: O(t + s)
    # Time: started 11:02
    def minWindow(self, s: str, t: str) -> str:
        count = 0
        answer = None
        freq = defaultdict(int)
        t_freq = defaultdict(int)
        for char in t:
            t_freq[char] += 1
        t_length = len(t_freq)

        left = 0
        for i in range(len(s)):
            freq[s[i]] += 1

            if freq[s[i]] == t_freq[s[i]]:
                count += 1

            while left <= i and count == t_length:
                if not answer or (i + 1) - left < len(answer):
                    answer = s[left:i + 1]

                if freq[s[left]] == t_freq[s[left]]:
                    count -= 1
                freq[s[left]] -= 1
                left += 1
            
        return answer if answer is not None else ""

        
solution = Solution()
answer = solution.minWindow("cabwefgewcwaefgcf", "aa")
answer = solution.minWindow("ADOBECODEBANC", "ABC")
print(answer)