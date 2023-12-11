from typing import List
from collections import deque

# https://leetcode.com/problems/add-strings/
# Tags: Deque
class Solution:

    # Runtime Complexity: O(max(n1,n2))
    # Space Complexity: O(max(n1,n2))
    # Time: 14:00
    def addStrings(self, num1: str, num2: str) -> str:
        output = deque()
        num1 = list(num1)
        num2 = list(num2)

        carry = 0
        while num1 or num2:
            c1 = c2 = 0
            if num1:
                c1 = ord(num1.pop()) - 48
            if num2:
                c2 = ord(num2.pop()) - 48

            s = c1 + c2 + carry
            if s > 9:
                carry = 1
                s -= 10
            else:
                carry = 0
            output.appendleft(str(s))
        if carry:
            output.appendleft("1")

        return "".join(output)

        
solution = Solution()
answer = solution.addStrings("1", "9")
print(answer)