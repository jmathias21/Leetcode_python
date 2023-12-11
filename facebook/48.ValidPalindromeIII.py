from typing import List
from collections import deque

# https://leetcode.com/problems/valid-palindrome-iii/
# Tags: BFS
class Solution:

    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # Time: Not timed
    def isValidPalindrome(self, s: str, k: int) -> bool:
        queue = deque([(0, len(s) - 1, 0)])
        visited = [[False for _ in range(len(s))] for _ in range(len(s))]

        while queue:
            l, r, depth = queue.popleft()

            if depth > k:
                return False

            while s[l] == s[r]:
                l += 1
                r -= 1
                if l >= r:
                    return True

            if not visited[l + 1][r]:
                queue.append((l + 1, r, depth + 1))
                visited[l + 1][r] = True
            if not visited[l][r - 1]:
                queue.append((l, r - 1, depth + 1))
                visited[l][r - 1] = True


        
solution = Solution()
answer = solution.isValidPalindrome("aaabaabaa", 1)
answer = solution.isValidPalindrome("abbababa", 1)
answer = solution.isValidPalindrome("abcdeca", 2)
print(answer)