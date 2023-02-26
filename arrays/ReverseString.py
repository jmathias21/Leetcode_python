from typing import List

# https://leetcode.com/problems/reverse-string/description/
# Tags: Two Pointers
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1

        print(s)


solution = Solution()
solution.reverseString(['t','e','s','t'])