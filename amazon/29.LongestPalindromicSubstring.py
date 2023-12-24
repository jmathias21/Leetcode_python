from typing import List

# https://leetcode.com/problems/longest-palindromic-substring/
# Tags: 
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O()
    # Time: started 4:17
    def longestPalindrome(self, s: str) -> str:
        stack = [(0,0)]
        longest = s[0]

        for i in range(1, len(s)):
            stack.append((i, i))
            if s[i - 1] == s[i]:
                stack.append((i - 1, i))
                longest = s[i - 1: i + 1]

        while stack:
            l, r = stack.pop()
            while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                l, r = l - 1, r + 1
                if r - l + 1 > len(longest):
                    longest = s[l: r + 1]

        return longest



        
solution = Solution()
answer = solution.longestPalindrome("adcbbcde")
print(answer)