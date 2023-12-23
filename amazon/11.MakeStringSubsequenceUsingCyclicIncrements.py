from typing import List

# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
# Tags: 
class Solution:

    # Runtime Complexity: O(max(s1, s2))
    # Space Complexity: O(1)
    # Time: 17:00
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        for char in str2:
            is_valid = False
            while i < len(str1):
                diff = ord(char) - ord(str1[i])
                if 0 <= diff < 2 or diff == -25:
                    is_valid = True
                    i += 1
                    break
                i += 1
            if not is_valid:
                return False
        return True

        
solution = Solution()
answer = solution.canMakeSubsequence("z", "a")
print(answer)