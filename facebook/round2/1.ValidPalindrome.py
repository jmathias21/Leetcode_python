from typing import List
import re

# https://leetcode.com/company/facebook
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 10:00
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[\W_]", "", s)
        s = s.lower()

        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    
        
solution = Solution()
answer = solution.isPalindrome("A man, a plan, a canal: Panama")
print(answer)