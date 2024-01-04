from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: started 8:50
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def is_valid_palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        while left < right:
            if s[left] != s[right]:
                return is_valid_palindrome(s[left + 1:right + 1]) or is_valid_palindrome(s[left:right])
            left += 1
            right -= 1

        return True

        
solution = Solution()
answer = solution.validPalindrome("cbafac")
answer = solution.validPalindrome("cafabc")
print(answer)