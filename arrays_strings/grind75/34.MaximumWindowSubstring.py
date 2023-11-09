from collections import Counter, defaultdict

# https://leetcode.com/problems/minimum-window-substring/
# Tags: Sliding window, hash map
class Solution:

    # Runtime Complexity: O(M + N)
    # Space Complexity: O(M + N)
    # Time: started 11:30
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        t_counts = Counter(t)
        window_counts = defaultdict(int)
        required = len(t_counts)
        count = 0
        # Use a tuple for our answer so we can build the sub-array just once
        answer = (float('inf'), 0, 0)

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            # determine if the current count of the current char matches t
            if char in t_counts and window_counts[char] == t_counts[char]:
                count += 1

            while left <= right and count == required:
                char = s[left]

                if right - left + 1 < answer[0]:
                    answer = (right - left + 1, left, right)

                window_counts[s[left]] -= 1
                if char in t_counts and window_counts[char] < t_counts[char]:
                    count -= 1

                left += 1
            right += 1

        return s[answer[1]:answer[2] + 1] if answer[0] != float('inf') else ""

        
solution = Solution()
answer = solution.minWindow("a", "a")
answer = solution.minWindow("ab", "b")
answer = solution.minWindow("ADOBECODEBANC", "ABC")
print(answer)