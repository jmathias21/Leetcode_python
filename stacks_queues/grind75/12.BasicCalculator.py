# https://leetcode.com/problems/basic-calculator/
# Tags: Recursion
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 42:00
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "") + "+"

        def rec(i):
            curr_num = 0
            sum = 0
            op = "+"
            while i < len(s):
                if s[i].isdigit():
                    curr_num *= 10
                    curr_num += int(s[i])
                else:
                    if s[i] == "(":
                        curr_num, i = rec(i + 1)
                    if op == "+":
                        sum += curr_num
                    if op == "-":
                        sum -= curr_num
                    if s[i] == ")":
                        return (sum, i + 1)
                    if s[i] in ("+", "-"):
                        op = s[i]
                    curr_num = 0
                i += 1

            return (sum, 0)

        answer, _ = rec(0)
        return answer

        
solution = Solution()
answer = solution.calculate("1 + 1")
answer = solution.calculate("(1+(4+5+2)-3)+(6+8)")
print(answer)