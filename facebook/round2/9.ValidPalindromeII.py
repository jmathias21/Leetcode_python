from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:30
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
            left += 1
            right -= 1
        return True

        
solution = Solution()
answer = solution.validPalindrome("abccdba")
print(answer)