import re

# https://leetcode.com/problems/valid-palindrome/
# Tags: regex
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    #
    # Loop up to halfway through the string and compare the beginning and ending
    # to each other and make sure they're the same. We can skip the last character
    # if the string length is odd because we'd be comparing the same character to
    # itself
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters and lowercase the string
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s).lower()

        n = len(s)
        for i in range(0, int(n / 2)):
            if s[i] != s[n - 1 - i]:
                return False
            
        return True

        
solution = Solution()
answer = solution.isPalindrome("ra,ce,c    ar")
answer = solution.isPalindrome("god")
print(answer)