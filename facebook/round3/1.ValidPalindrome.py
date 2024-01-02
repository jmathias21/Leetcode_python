from typing import List
import re

# https://leetcode.com/problems/valid-palindrome/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Started 11:05
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                new_str += char
        new_str = new_str.lower()

        left = 0
        right = len(new_str) - 1

        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
            
        return True


        
solution = Solution()
answer = solution.isPalindrome("A man, a plan, a canal: Panama")
print(answer)