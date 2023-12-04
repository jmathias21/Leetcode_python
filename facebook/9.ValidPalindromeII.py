# https://leetcode.com/problems/valid-palindrome-ii/
# Tags: Two pointers
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 30:00
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def checkPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while left <= right:
            if s[left] != s[right]:
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)
            left += 1
            right -= 1
            
        return True


        
solution = Solution()
answer = solution.validPalindrome("eccer")
answer = solution.validPalindrome("ebcbbececabbacecbbcbe")
answer = solution.validPalindrome("ebcbbececabbacecbbcbe")
answer = solution.validPalindrome("ab")
answer = solution.validPalindrome("eabbcae")
print(answer)