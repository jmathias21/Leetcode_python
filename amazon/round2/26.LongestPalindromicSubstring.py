from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O()
    # Time: started 3:23
    def longestPalindrome(self, s: str) -> str:
        stack = [(0,0)]
        longest = s[0]

        for i in range(1, len(s)):
            stack.append((i, i))
            if s[i] == s[i - 1]:
                stack.append((i - 1, i))

        for l, r in stack:
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                if r - l + 1 > len(longest):
                    longest = s[l:r + 1]

                l -= 1
                r += 1

        return longest

        
solution = Solution()
answer = solution.longestPalindrome("babad")
answer = solution.longestPalindrome("abadaba")
print(answer)