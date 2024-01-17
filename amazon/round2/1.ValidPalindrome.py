from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 10:17
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for char in s:
            if char.isalpha() or char.isdigit():
                new_str += char

        new_str = new_str.lower()

        left, right = 0, len(new_str) - 1
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            else:
                left += 1
                right -= 1

        return True

        
solution = Solution()
answer = solution.isPalindrome("A man, a plan, a canal: Panama")
print(answer)