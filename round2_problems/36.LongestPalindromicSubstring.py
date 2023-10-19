from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 12:58
    def longestPalindrome(self, s: str) -> str:
        stack = [(0, 0)]
        longest = ''

        for i in range(1, len(s)):
            stack.append((i, i))
            if s[i] == s[i - 1]:
                stack.append((i - 1, i))

        for left, right in stack:
            while True:
                if left < 0 or right >= len(s):
                    break

                if s[left] != s[right]:
                    break

                if len(longest) < (right - left) + 1:
                    longest = s[left:right + 1]

                left, right = left - 1, right + 1

        return longest

        
solution = Solution()
answer = solution.longestPalindrome("cbbd")
answer = solution.longestPalindrome("babbad")
print(answer)