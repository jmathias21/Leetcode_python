from typing import List

# https://leetcode.com/problems/valid-palindrome/
# Tags:
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 11:24
    def isPalindrome(self, s: str) -> bool:
        new_str_arr = []
        for char in s:
            if char.isalpha() or char.isdigit():
                new_str_arr.append(char.lower())

        new_str = "".join(new_str_arr)
        return new_str == new_str[::-1]

        
solution = Solution()
answer = solution.isPalindrome("0P")
answer = solution.isPalindrome("A man, a plan, a canal: Panama")
print(answer)