from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n ^ 2)
    # Space Complexity: O(n)
    # Time: 18:00
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s[0]

        queue = deque([(0,0)])
        longest = [s[0]]

        for i in range(1, len(s)):
            queue.append((i,i))
            if s[i - 1] == s[i]:
                queue.append((i - 1, i))
                longest = s[i - 1:i + 1]

        while queue:
            l1, l2 = queue.popleft()
            left = l1 - 1
            right = l2 + 1

            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break

                if right - left > len(longest) - 1:
                    longest = s[left:right + 1]

                left -= 1
                right += 1

        return "".join(longest)

        
solution = Solution()
answer = solution.longestPalindrome("aaaaa")
answer = solution.longestPalindrome("ac")
answer = solution.longestPalindrome("cbbd")
answer = solution.longestPalindrome("babad")
print(answer)