from typing import List

# https://leetcode.com/problems/reverse-integer/
# Tags: Math
class Solution:

    # Runtime Complexity: O(logn)
    # Space Complexity: O(n)
    # Time: 10:00
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)

        reversed_num = 0
        while x > 0:
            last_digit = x % 10
            x //= 10
            reversed_num *= 10
            reversed_num += last_digit

        if reversed_num > 2 ** 31:
            return 0

        return -reversed_num if is_negative else reversed_num


        
solution = Solution()
answer = solution.reverse(1534236469)
answer = solution.reverse(123)
print(answer)